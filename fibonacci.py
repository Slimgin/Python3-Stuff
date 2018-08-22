#! /usr/bin/env Python3

def fib(n):	# Write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a) # Removed ", end=' '"
        a, b = b, a+b
    print()
