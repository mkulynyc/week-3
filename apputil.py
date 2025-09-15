import seaborn as sns
import pandas as pd

"""
Exercise 1: Recursive Fibonacci Function

This fib(n) function recursively calculates the nth Fibonacci number.

Arguments:
- n: An integer representing the position in the Fibonacci sequence.

Returns:
- The nth Fibonacci number.
"""

def fib(n):
    # Return 0 if n is 0
    if n <= 0:
        return 0
    
    # Return 1 if n is 1 (1st Fibonacci number)
    elif n == 1:
        return 1
    
    # Otherwise, return the sum of the 2 preceding Fibonacci numbers recursively
    else:
        return fib(n - 1) + fib(n - 2)
    

"""
Exercise 2: Integer to Binary conversion

This to_binary(x) function recursively converts an integer to binary

Arguments: 
- x: An integer to be converted to binary.

Returns:
- A string representing the binary equivalent of the integer.
"""

def to_binary(x):
    # Base case 1: if x is 0, return 0
    if x == 0:
        return "0"
    
    # Base case 2: if x is 1, return 1
    elif x == 1:
        return "1"
    
    # Recursive case: integer divide x by 2 and append the remainder of x divided by 2
    else:
        return to_binary(x // 2) + str(x % 2)
    
