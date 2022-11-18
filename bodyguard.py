#! /usr/bin/env Python3

import re

#test = re.compile('[A-Za-z]{4}')
#pattern = '^[A-Za-z]*$'
data = open('bodyguard.txt').read()

print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))
#re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)

#with open('test.txt') as file_obj:
#	contents = file_obj.read()
#	something = pattern.findall(contents)
#	for letter in something:
#		if letter[0] == letter[-1]:
#			print(something)