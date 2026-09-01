# in robber house 2 => 1st ko rob karega toh last ko rob nhi karega
# 2nd ko rob karega toh last ko rob kar sakta hai

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            memo = {}
            def dp(i):
                if i < 0:
                    return 0
                if i == 0:
                    return arr[0]
                if i in memo:
                    return memo[i]
                
                robNhiKra = dp(i-1)
                robKra = dp(i-2) + arr[i]
                memo[i] = max(robNhiKra, robKra)
                return memo[i]
            return dp(len(arr)-1)

        # Case 1: exclude last
        case1 = helper(nums[:-1])
        # Case 2: exclude first
        case2 = helper(nums[1:])
        return max(case1, case2)
