# in robber house 2 => 1st ko rob karega toh last ko rob nhi karega
# 2nd ko rob karega toh last ko rob kar sakta hai

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def rob_linear(houses):
            prev1 = 0
            prev2 = 0
            for money in houses:
                # skip or do not skip
                curr = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = curr
                
            return prev1
        # 0 to n-2 # exlude last
        case1 = rob_linear(nums[:-1])
        # 1 to n # exclude first
        case2 = rob_linear(nums[1:])

        return max(case1, case2)