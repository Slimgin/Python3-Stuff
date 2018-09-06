#! /usr/bin/env Python3
import binascii
import string

list1 = []
number = 0
list_pos = 0
#key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encoded_string = bytes.fromhex(input('Please enter the cipher stream: '))

#print(encoded_string)
#print(type(encoded_string))
for byte in encoded_string:
	list1.insert(list_pos, ord(string.ascii_lowercase[number]) ^ byte)
	list_pos += 1
print(string.ascii_lowercase[number])
number += 1
print("*" * len(encoded_string))
for item in list1:
	print(chr(item), end = " ")
