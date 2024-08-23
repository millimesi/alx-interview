#!/usr/bin/env python3


# Calculating factorial with two methods
# here the itretive way is better in terms of space

def recur_factorial(n):

    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

def itrative_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        fact = 1
        for i in range(2, n+1):
            fact *= i
        return fact

print(recur_factorial(6))
print(itrative_factorial(6))
