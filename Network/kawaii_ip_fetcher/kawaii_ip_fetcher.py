#!/bin/python3
import pyfiglet
import urllib.request
import requests
import json

text = "KAWAII IP FETCHER"
ascii_art = pyfiglet.figlet_format(text)
print(ascii_art)

external_ip = urllib.request.urlopen('https://ipv4.icanhazip.com/').read().decode('utf8')

def nl(): print('\n')

request_url = 'https://geolocation-db.com/jsonp/' + external_ip
response = requests.get(request_url)
result = response.content.decode()
result = result.split("(")[1].strip(")")
result  = json.loads(result)

matrix = "Follow the white rabbit"
ascii1 = """ (\ /) """
ascii2 = """ ( . .) """
ascii3 = """C(")(") """
print(matrix)
nl()
print(ascii1)
print(ascii2)
print(ascii3)
nl()
print("Your ip address is : " + format(external_ip))
print(result)
