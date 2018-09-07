#! /usr/bin/env Python3

import string
import binascii


encoded_string = bytes.fromhex(input('Please enter the cipher stream: '))
#list_pos = 0
#list = []
<<<<<<< HEAD
#key = string.ascii_uppercase
key = 'X'
=======
key = string.ascii_uppercase
#key = 'X'
>>>>>>> c15d5dd8c755a1faa09b11cb4e3dc921a82902be
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