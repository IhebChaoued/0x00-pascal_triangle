#!/usr/bin/python3


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

    # Initialize the dp array with infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Compute the minimum coins needed for each amount up to total
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, return -1 indicating it's not possible
    return dp[total] if dp[total] != float('inf') else -1
