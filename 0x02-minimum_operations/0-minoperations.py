#!/usr/bin/python3
''' minimum operation module '''


def minOperations(n):
    '''
    computes mimum operations needed to compute n times of copies
    Args:
        n(int): number of copies of H
    return:
        (int): minimum operations
    '''
    if n <= 1:
        return 0

    ops = 0
    fact = 2

    while n > 1:
        while n % fact == 0:
            ops += fact
            n //= fact
        fact += 1

    return ops
