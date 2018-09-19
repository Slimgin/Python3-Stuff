#! /usr/bin/env Python3

import re

test = re.compile('[A-Z]{3}')

with open('test.txt') as file_obj:
	contents = file_obj.read()
	something = test.findall(contents)
	for letter in something:
		if letter[0] == letter[2]:
			print(something)