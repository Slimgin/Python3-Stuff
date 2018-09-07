#! /usr/bin/env Python3

dict1 = {}

statement = 'This is a statement that is going to be parsed into a dictionary. The quick brown fox jumps over the lazy dog'

for i in statement:
    if i in dict1.keys():
        dict1[i] += 1
    else:
        dict1[i] = 1

print(dict1)