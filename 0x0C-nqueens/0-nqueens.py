#!/usr/bin/python3

import sys


def nqueens(queens, cl_queens, sum):
    """Finds all valid queen column positions
    """
    count = len(queens)
    if count == n:
        queen_col.append(queens)
        return None
    for resolve in range(n):
        if resolve not in queens and count - resolve not in cl_queens and count + resolve not in sum:
            nqueens(queens + [resolve], cl_queens + [count - resolve], sum + [count + resolve])


def parse_argv():
    """Checks for usage errors"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


if __name__ == "__main__":
    n = parse_argv()
    queen_col = []
    nqueens([], [], [])
    for row in range(len(queen_col)):
        queen_pos = []
        for col in range(len(queen_col[row])):
            queen_pos.append([col, queen_col[row][col]])
        print(queen_pos)
