#!/usr/bin/python3
"""MAKE CHANGE"""


def makeChange(coins, total):
    """
    Finds the fewest number of coins needed to make the given total.

    Parameters:
    coins (list): Values of available coins.
    total (int): The target amount.

    Returns:
    int: Minimum number of coins needed, or -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
