# https://www.youtube.com/watch?v=X50Rknzenus
# in dp array we will have answer to
# if we include current element -> s - num => with the remaing is there
# subset sum possible if yes then include current element. By adding current
# element we will reach the target
# condition to exclude the element is => s - num -> with the remaining is
# subset sum possible. If NO then exclude the current element. 
class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            # nums - 1 ke baad substraction will give -ve sum, which is of
            # no use
            for s in range(target, num - 1, -1):
                print(f"s = {s}")
                print(f"num = {num}")
                if dp[s - num]:  # s = num - 1 => num - 1 - num = -1
                    dp[s] = True
        
        return dp[target]
