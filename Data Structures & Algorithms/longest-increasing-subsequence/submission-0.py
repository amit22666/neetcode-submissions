class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # ith index -> 0 to n
        # jth indeth -> 0 to i
#intution - we are at i and we know the len of lis of each index before i.
# we use that info to get len of lis at ith
# max for that lis array will be the answer.
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1,dp[i])
        
        return max(dp)
                    
