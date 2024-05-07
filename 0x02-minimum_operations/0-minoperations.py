#!/usr/bin/python3
"""Minimum Operations module"""


def minOperations(n: int) -> int:
    """Calculates the fewest number of operations"""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations


if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(
        n, minOperations(n)
        ))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(
        n, minOperations(n)
        ))
