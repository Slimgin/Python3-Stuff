#! /usr/bin/env Python3

#  #1
def max_of_two(x, y):
	if x > y:
		return x
	return y
#print(max_of_two(0, -1))

#  #2
def list_sum(sum):
	sum = 0
	for num in list_sum: # type: ignore
		sum = num + sum
	return sum
#num_list = [8, 2, 3, 0, 7] My code
#print(list_sum(sum)) My code
#print(sum((8, 2, 3, 0, 7))) # print(sum()) returns  an error - sum expected at most 2 arguments, got 5

#  #3
def multiply(numbers):
	product = 1
	for num in numbers:
		product *= num
	return numbers
#print(multiply((8, 2, 3, -1, 7)))

#  #4
def string_reverse(str1):
	rstr1 = ''
	index = len(str1)
	while index > 0:
		rstr1 += str1[index -1]
		index = index - 1
	return rstr1
print(string_reverse('1234abcd'))

''' The below doesnt work because there are no functions to do the work.
def string(reverse):
	rstr1 = string_reverse[::-1]
	return rstr1
print(string_reverse('1234abcd')'''

#  #5
import math
num = int(input('Please input a number: '))
x = 1
def factorial(x):
	x = math.factorial(num)
	return x
print('The factorial of {} is: {}'.format(num, x))
