class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n + 1] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            square = 1

            while square * square <= target:
                dp[target] = min(
                    dp[target],
                    1 + dp[target - square * square]
                )
                square += 1

        return dp[n]