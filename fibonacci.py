""" Example of a recursive function to calculate the Fibonacci sequence. """

import pandas as pd

def fibonacci(n):
    """ Fibonacci series using recursion. """
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
#print(fibonacci(30))

pd.read_csv('D:/Cursus/VisualStudioCode_(Udemy)/_exercises/Python/data/example.csv')
