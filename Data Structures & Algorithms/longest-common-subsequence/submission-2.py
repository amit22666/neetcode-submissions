class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m, n = len(text1), len(text2)
        
        # dp[i][j] = LCS length for text1[0..i-1], text2[0..j-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill DP table bottom-up
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                if text1[i - 1] == text2[j - 1]:
                    # characters match ho gaye → 1 + diagonal value
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # match nahi hua → best of upar ya left
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # dp[m][n] hi final answer hai
        return dp[m][n]