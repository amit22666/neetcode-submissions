class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Transpose
        # row -> column and column -> row

        # reverse then we will get rotate image

        # Transpose
        # swap around diagonal
        n = len(matrix)
        m = len(matrix[0])
        arr = matrix
        for i in range(n):
            for j in range(i, m):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

        for i in range(n):
                arr[i].reverse()
