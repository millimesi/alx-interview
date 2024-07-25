#!/usr/bin/python3
"""
alx interview
"""


def makeChange(coins, total):
    """
    Function Determins the lowest coin
    Args:
        coins: list of values
        total: total value

    Returns:
        total number of coins
    """
    if (total <= 0):
        return 0

    dynamic_prog = [float('inf')] * (total + 1)
    dynamic_prog[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dynamic_prog[i] = min(dynamic_prog[i], dynamic_prog[i - coin] + 1)

    return dynamic_prog[total] if dynamic_prog[total] != float('inf') else -1
