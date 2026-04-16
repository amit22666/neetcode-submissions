# 4 things need to figure out - choices, constraints, base case, backtrack step

# choices: 
#     one queen per column
#     choose a row for each queen
# Constaint:
    



# A queen attacks in 3 independent directions:
# column, main diagonal, anti-diagonal.
# Each needs its own constraint tracking.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        # Sets to track attacks
        cols = set()        # columns
        diag1 = set()       # (row - col)  → main diagonal
        diag2 = set()       # (row + col)  → anti diagonal

        # Logic that checks diagonals, rows and cols
        def is_valid(row, col):
            if col in cols:
                return False
            if (row - col) in diag1:
                return False
            if (row + col) in diag2:
                return False
            return True

        # remove last queen we placed
        def backtrack(row):
            if row == n:
                # convert board to required output format
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                if not is_valid(row, col):
                    continue

                # place queen
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                # backtrack (remove queen)
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return result
