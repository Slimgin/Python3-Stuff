'''
Fibonacci Series output to list
'''



'''
# Code block does not print the right sequence. Use fibindex(n) instead.
#!/usr/bin/env python3

def fib2(n):	# Write Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # Appending each new a result to end of list.
        a, b = b, a+b
    result.pop(0)
    return result

'''


'''
Fibonacci series to a given index number.

Index -     1 2 3 4 5 6 7  8  9  10 11
Fibonacci - 0 1 1 2 3 5 8  13 21 34 55
'''


def fibindex(n):
    index = []
    a, b = 0, 1
    count = 0
    while count <= n:
        index.append(a)
        a, b = b, a+b
        count += 1
    index.pop(0)
    return index

def fibseq(n):
    index = [0, 1]
    count = 3
    while count <= n:
        c = index.__getitem__(-2) + index.__getitem__(-1)
        index.append(c)
        count += 1
    return index
    