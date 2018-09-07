'''
Fibonacci Series output to list
'''

#! /usr/bin/env Python3

def fib2(n):	# Write Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # Appending each new a result to end of list.
        a, b = b, a+b
    return result
