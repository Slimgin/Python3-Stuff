#! /usr/bin/env Python3

characters = {}
value = 1
with open('rare.txt') as file_obj:
	contents = file_obj.read()
	for char in contents:
		if char not in characters.keys():
			characters[char] = 1
		else:
			characters[char] += 1
print(characters)