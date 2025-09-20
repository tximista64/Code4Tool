#!/usr/bin/env python3
from base64 import b64decode
from Crypto.Cipher import ARC4  
import sys

job_b64 = "B//jOYkMjUR2wj+L/9U9WafJi7K/GMIoeILXOeXYfdGUMV8eNqoLdrQlZ35neKaqiGJ4Vijv4WuInBYFg1nnW9sY0sdq0imYHI1jW+skjZIgz3ICgNSxOkxRTpwzCA=="
key = "WkZPxBoH6CA3Ok4iI"

ct = b64decode(job_b64)
cipher = ARC4.new(key.encode('utf-8'))
pt = cipher.decrypt(ct)
try:
    print(pt.decode('utf-8'))
except:
    print(pt)

