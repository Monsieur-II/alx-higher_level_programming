#!/usr/bin/python3
"""Solves nqeens problem"""


class Chess:
    @staticmethod
    def nQueens(n):
        # n is the size of nxn chess board
        columns = set()
        posConsts = set()
        negConsts = set()
        board = [[] for i in range(n)]

        def backtrack(r):
            # we will only get to this point if all rows (row 0 to row n - 1) found a free spot
            if r == n:
                copy = board.copy()
                print(copy)
                return

            for c in range(n):
                if c in columns or (r + c) in posConsts or (r - c) in negConsts:
                    continue

            # if the current column or the diagonal constants of current position are not taken
            # fill it else, move to next column

                columns.add(c)
                posConsts.add(r + c)
                negConsts.add(r - c)
                board[r].append(r)
                board[r].append(c)

                # after filling perform an iteration for the next ROW
                # If the next row finds a free space it will take it and call the next row

                backtrack(r + 1)

                # At this point, all possible child solutions under this position,(r, c) have been made
                # so we clear the filled position, after removing column and diagonal constants from
                # respective sets{}. Then move to the next column and repeat.

                columns.remove(c)
                posConsts.remove(r + c)
                negConsts.remove(r - c)
                board[r].clear()

        backtrack(0)


if __name__ == "__main__":

    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    Chess.nQueens(N)
