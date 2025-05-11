#!/bin/python3

import base64
import sys
import pyfiglet
from termcolor import colored

text = colored("Please enter your Base64 to decode", "light_magenta", attrs=["bold"])
text2 = "DONE"
ascii_art = pyfiglet.figlet_format(text2)

print(text)
decode = input()
print(base64.b64decode(decode))
print(ascii_art)

