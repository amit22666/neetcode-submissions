# https://www.youtube.com/watch?v=X50Rknzenus

class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            # go backwards to avoid overwriting
            for s in range(target, num - 1, -1):
                print(f"s = {s}")
                print(f"num = {num}")
                if dp[s - num]:
                    dp[s] = True
        
        return dp[target]
