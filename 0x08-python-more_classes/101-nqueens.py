#!/usr/bin/python3


import sys
def validate_input():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    return N

def is_safe(board, row, col, N):
    # Check if it's safe to place a queen at (row, col)
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens_util(board, row, N):
    if row == N:
        print_solution(board, N)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_n_queens_util(board, row + 1, N)

def solve_n_queens(N):
    board = [-1] * N
    solve_n_queens_util(board, 0, N)

def print_solution(board, N):
    for i in range(N):
        line = ["Q" if j == board[i] else "." for j in range(N)]
        print("".join(line))
    print()