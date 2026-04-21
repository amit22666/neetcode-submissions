class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        rowsToZero = set()
        colsToZero = set()

        # Step 1: Traverse karo aur zero cells identify karo
        # Agar matrix[r][c] == 0 hai toh us row aur column ko mark kar lo
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rowsToZero.add(r)
                    colsToZero.add(c)

        # Step 2: Traverse karo aur marked rows/cols ko zero set kar do
        for r in range(rows):
            for c in range(cols):
                if r in rowsToZero or c in colsToZero:
                    matrix[r][c] = 0
