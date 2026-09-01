class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def helper(i):
            if i < 0:
                return 0
            if i == 0:
                return nums[0]
            
            if i in memo:
                return memo[i]
            
            robNhiKra = helper(i-1) # rob nhi kra
            robKra = helper(i-2) + nums[i]
            memo[i] = max(robNhiKra,robKra)
            return memo[i]
        return helper(len(nums) - 1)