class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (cols + 1) for _ in range(rows + 1)]  

        
        
        for r in range(rows):
            for c in range(cols):
                self.sumMat[r + 1][c + 1] = (
                    self.sumMat[r][c + 1]     # top
                    + self.sumMat[r + 1][c]   # left
                    - self.sumMat[r][c]       # overlap
                    + matrix[r][c]            # ✅ missing value
                )


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # prefix sum matrix
        # issue first row and first column
        # Approach 1 - padding, Approach 2 - calculate first
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        ans = self.sumMat[row2][col2] - self.sumMat[row1-1][col2] - self.sumMat[row2][col1-1]  + self.sumMat[row1-1][col1-1]
        return ans


        # then o(1) answer


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)