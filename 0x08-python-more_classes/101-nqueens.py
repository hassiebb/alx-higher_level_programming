#!/usr/bin/python3
"""A module that solves the N-Queens problem"""

import sys

def is_safe(board, row, col, n):
    # Check if the current position is safe for the queen
    # Check for column attacks
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check for left diagonal attacks
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check for right diagonal attacks
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row, n):
    if row == n:
        # Print the solution
        for i in range(n):
            print(' '.join(board[i]))
        print()
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen and move to the next row
            board[row][col] = 'Q'
            solve_nqueens(board, row+1, n)
            # Backtrack and remove the queen
            board[row][col] = '.'

def nqueens(n):
    # Create an empty chessboard
    board = [['.' for _ in range(n)] for _ in range(n)]

    # Solve the N-Queens problem
    solve_nqueens(board, 0, n)

if __name__ == '__main__':
    # Check the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Solve the N-Queens problem
    nqueens(n)
