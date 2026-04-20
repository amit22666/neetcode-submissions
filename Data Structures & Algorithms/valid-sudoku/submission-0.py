from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowmap = {i: set() for i in range(9)}
        colmap = {j: set() for j in range(9)}
        boxmap = {(i, j): set() for i in range(3) for j in range(3)}

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                if (
                    val in rowmap[i]
                    or val in colmap[j]
                    or val in boxmap[(i // 3, j // 3)]
                ):
                    return False

                rowmap[i].add(val)
                colmap[j].add(val)
                boxmap[(i // 3, j // 3)].add(val)

        return True