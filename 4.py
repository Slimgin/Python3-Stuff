#! /usr/bin/env Python3

import string
import binascii
import sys
import os
cnt = 1
decoded = {}
key = []
chars = 0
non_chars = 0

key.extend(list(string.ascii_lowercase)+list(string.ascii_uppercase))



filepath = '4.txt'
f = open(filepath).readlines()
f = [x.strip('\n') for x in f]
for line in f:
	encoded_string = bytes.fromhex(line)
	#print("Line {}: {} as hex {}".format(cnt,line, bytes.fromhex(line)))
	cnt += 1

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
		if score <= 40:
			print(letter + ':' + "*" * 50) # Added this line to denote which letter did the decrypt
			print('\n')
			print(decoded)
			print('\n')
			#print(decode, end='')
			#print('\n')
			print("The non-character score is: " + str(int(score)) + " The lower the better.")
			decoded = {}
			chars = 0
			non_chars = 0
		else:
			decoded = {}
			chars = 0
			non_chars = 0