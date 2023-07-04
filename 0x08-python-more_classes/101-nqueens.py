#!/usr/bin/python3
"""Solves nqeens problem"""


class Chess:
    @staticmethod
    def nQueens(n):
        columns = set()
        positiveConstants = set()
        negativeConstants = set()
        board = [[] for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = board.copy()
                print(copy)
                return

            for c in range(n):
                if c in columns or (r + c) in positiveConstants or
                (r - c) in negativeConstants:
                    continue

                columns.add(c)
                positiveConstants.add(r + c)
                negativeConstants.add(r - c)
                board[r].append(r)
                board[r].append(c)

                backtrack(r + 1)

                columns.remove(c)
                positiveConstants.remove(r + c)
                negativeConstants.remove(r - c)
                board[r].clear()

        backtrack(0)


if __name__ == "__main__":

    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    N = sys.argv[1]
    if not N.isdigit():
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    Chess.nQueens(N)
