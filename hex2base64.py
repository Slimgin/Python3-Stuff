'''
Script for Challenge 1 Set 1
'''

#! /usr/bin/env Python3

"""
Python script to convert hex values to base64
To run this script as it is, 'from hex2base64 import hexstring_to_b64' && 'import base64'
Assign a hex value to string 'string = "ffff"
Run 'hexstring_to_b64(string)
"""

import base64

def hexstring_to_b64(string):

    decoded_hexstring = bytes.fromhex(string)
    b64_encoded_string = base64.b64encode(decoded_hexstring)
    return b64_encoded_string.decode()
