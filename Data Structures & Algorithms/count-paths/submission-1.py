
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] = (i, j) tak pahunchne ke total unique paths
        # Base: first row/first column mein sirf 1 hi tareeka hota hai (straight right ya straight down)

        dp = [[1] * n for _ in range(m)]  # sabko 1 se init kyunki edges par 1 hi raasta hota hai

        # Ab inner cells ke liye: upar + left se aakar total paths
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # Last cell hi answer hai
        return dp[m - 1][n - 1]
