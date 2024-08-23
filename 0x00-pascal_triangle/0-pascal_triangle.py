#!/usr/bin/python3
"""Pascal's triangle"""


def factorial(n):
    """ Compute factorial using loops
    Args:
        n(int): number need to be factorial
    returns:
        (int): fatorial of the number
    """
    if n == 1 or n == 0:
        return 1
    else:
        fact = 1
        for i in range(2, n+1):
            fact *= i
        return fact


def binomial_function(i, j):
    """ Compute the binomial coefficient
    Args:
        n(int): The total number of items.
        k(int): The number of items to choose.
    Returns:
        (int): The binomial coefficient.
    """
    return factorial(i) // (factorial(j) * factorial(i - j))


def pascal_triangle(n):
    """
    create list of pascal's triangls
    Args:
        n(int): number of rows
    retuns:
        List[List(int)]: 2D list the pascal's triangle
    """
    if n <= 0:
        return []

    outer_list = []
    for i in range(n):
        inner_list = []
        for j in range(i + 1):
            # permutuatuion
            value = binomial_function(i, j)
            inner_list.append(value)
        outer_list.append(inner_list)

    return outer_list
