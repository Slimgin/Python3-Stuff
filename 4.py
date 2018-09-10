#! /usr/bin/env Python3

import string
import sys
import os


filepath = sys.argv[2]
with open(filepath) as f:
	for line in f:
		print("Line: {} as hex {}".format(line, bytes.fromhex(line))