#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    def sieve(n):
        """ Sieve of Eratosthenes to find all primes less than n """
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
        return prime_numbers

    def play_game(n):
        """ Play a single game with n and return the winner """
        primes = sieve(n)
        is_prime = [False] * (n + 1)
        for p in primes:
            is_prime[p] = True

        moves = 0
        for num in range(2, n + 1):
            if is_prime[num]:
                moves += 1
                for multiple in range(num, n + 1, num):
                    is_prime[multiple] = False

        return 'Maria' if moves % 2 == 1 else 'Ben'

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
