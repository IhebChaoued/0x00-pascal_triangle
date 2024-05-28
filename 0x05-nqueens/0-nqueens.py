#!/usr/bin/python3
"""N Queens"""
import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col]
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col, n):
    """
    Recursive utility function to solve N Queens problem
    """
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens(board, col + 1, n):
                return True
            board[i][col] = 0

    return False


def print_solution(board, n):
    """
    Print the solution
    """
    solutions = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solutions.append([i, j])
    print(solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens(board, 0, n) is False:
        print("No solution exists")
        sys.exit(1)

    print_solution(board, n)
