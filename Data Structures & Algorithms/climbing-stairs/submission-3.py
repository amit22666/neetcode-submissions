# You are given an integer n representing the number of steps to reach the top of a staircase. 
# You can climb with either 1 or 2 steps at a time.
# Return the number of distinct ways to climb to the top of the staircase.

# total => number of distinct ways

# ith -> (i - 1) + (i - 2)

class Solution:
    # def climbStairs(self, n: int) -> int:
    #     def dfs (n):
    #         if n == 0 or n == 1:
    #             return 1 
    #         oneStepWays = dfs(n-1)
    #         twoStepWays = dfs(n-2)
    #         return oneStepWays + twoStepWays
    #     return dfs(n)

    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]