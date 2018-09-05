#! /usr/bin/env Python3

"""
Python script to XOR equal length HEX strings
To run this script as it is, 'from hex2base64 import hexstring_to_b64' && 'import base64'
Assign a hex value to string 'string = "ffff"
Run 'hexstring_to_b64(string)
>>> hex(int(string1, 16) ^ int(string2, 16))
'0xdd42218c5358e7d2'
"""

hex1 = input('Please enter the first HEX number: ')
hex2 = input('Please enter the second HEX number: ')

xor_value = hex(int(hex1, 16) ^ int(hex2, 16))
print("The XOR'd value is " + xor_value[2:])
