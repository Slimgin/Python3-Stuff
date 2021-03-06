'''
Please use this file instead of single-byte_xor.py
'''

#! /usr/bin/env Python3

import string
import binascii
decoded = {}
key = []
chars = 0
non_chars = 0


encoded_string = bytes.fromhex(input('Please enter the cipher stream: ')) 
'''
Use 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736 for user input.
'''
#key = 'X'
key.extend(list(string.ascii_lowercase)+list(string.ascii_uppercase))

for letter in key:
	for byte in encoded_string:
		decode = chr(ord(letter) ^ byte)
		for i in decode:
			if i in decoded.keys():
				decoded[i] += 1
			else:
				decoded[i] = 1
    #print(decoded.keys())
	for i in decoded.keys():
		value = ord(i)
		if 65 <= value <= 90 or 97 <= value <= 122:
			chars += 1
		else:
			non_chars += 1
	score = (non_chars/chars)*100
	if score <= 15:
		print(letter + ':' + "*" * 50) # Added this line to denote which letter did the decrypt
		print('\n')
		print(decoded)
		print('\n')
		print("The non-character score is: " + str(int(score)) + " The lower the better.")
		decoded = {}
		chars = 0
		non_chars = 0
	else:
		decoded = {}
		chars = 0
		non_chars = 0

decode_letter = input('What letter do you want to use to decode this stream? ')
for byte in encoded_string:
	print(chr(ord(decode_letter) ^ byte), end='')

        
        
'''
Use this code instead to determine XOR value:

	Also, do different functions for XOR, score, and key_xor (letter to decrypt)

for i in range(256):
        b2 = [i] * len(b1)
        plaintext = bytes(xor(b1, b2))
        pscore = score(plaintext)
'''        
