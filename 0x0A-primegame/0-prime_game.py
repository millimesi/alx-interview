#!/usr/bin/python3
""" Prime numer game"""
from typing import List, Optional


def SieveOfEratosthenes(n: int) -> List[int]:
    '''
    list all prime number less than or equal to n
    Args:
        n(int): maximum range for prime numbers
    '''
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] is True):
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1

    return [p for p in range(2, n + 1) if prime[p]]


def isWinner(x: int, nums: List[int]) -> Optional[str]:
    """
    Determines the winner prime game

    Args:
        x (int): Number of rounds.
        nums (list): List of n of round.

    Returns:
        str: Name the winner ('Maria' or 'Ben') or return None.
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = SieveOfEratosthenes(max_n)

    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1]
        if i in primes:
            prime_counts[i] += 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
