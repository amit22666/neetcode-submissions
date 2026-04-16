

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # dp array contains -> answer to subproblem
        # at (i,j) what is the answer using previous values
        # now in the end i,j becomes m,n
        dp = [[1] *n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]  
        
        return dp[m-1][n-1]