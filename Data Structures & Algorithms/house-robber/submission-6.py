class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def helper(n):
            if n < 0:
                return 0
            if n == 0:
                return nums[0]
            
            if n in memo:
                return memo[n]
            
            robNhiKra = helper(n-1) # rob nhi kra
            robKra = helper(n-2) + nums[n]
            memo[n] = max(robNhiKra,robKra)
            return memo[n]
        return helper(len(nums) - 1)