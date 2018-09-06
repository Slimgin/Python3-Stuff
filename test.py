#! /usr/bin/env Python3

import string
import binascii


encoded_string = bytes.fromhex(input('Please enter the cipher stream: '))
#list_pos = 0
#list = []
key = string.ascii_uppercase
#key = 'X'
for letter in key:
    for byte in encoded_string:
        decoded = chr(ord(letter) ^ byte)
        #print(letter + "-" + "*" * 50, end='')
        print(decoded, sep='', end='')
        
        
        
        
        
"""        
        list.insert(list_pos, ord(letter) ^ byte)
        list_pos += 1
        #print(letter + " * " * len(encoded_string))
    #for item in list:
    print(chr(list), end = " ")
"""