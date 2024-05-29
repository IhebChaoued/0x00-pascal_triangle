#!/usr/bin/python3
"""N Queens"""
import sys


def print_usage_and_exit():
    """Print usage message and exit"""
    print("Usage: nqueens N")
    sys.exit(1)


def main():
    """Main function"""
    if len(sys.argv) != 2:
        """Check number of arguments"""
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        """Check if N is an integer"""
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        """Check if N is at least 4"""
        print("N must be at least 4")
        sys.exit(1)

    def print_solution(board):
        """Print the board solution"""
        solution = []
        for row in range(N):
            for col in range(N):
                if board[row][col] == 1:
                    solution.append([row, col])
        print(solution)

    def is_safe(board, row, col):
        """Check if position is safe for queen"""
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve_nqueens(board, col):
        """Solve N queens problem with backtracking"""
        if col >= N:
            print_solution(board)
            return True
        res = False
        for i in range(N):
            if is_safe(board, i, col):
                board[i][col] = 1
                res = solve_nqueens(board, col + 1) or res
                board[i][col] = 0
        return res

    board = [[0] * N for _ in range(N)]
    solve_nqueens(board, 0)


if __name__ == "__main__":
    main()
