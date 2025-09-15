import seaborn as sns
import pandas as pd


# update/add code below ...

"""
Exercise 1: Recursive Fibonacci Function

This function recursively calculates the nth Fibonacci number.

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
    


