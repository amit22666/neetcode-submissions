class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i, remaining):
            if i == len(nums):
                return 1 if remaining == 0 else 0

            # Choose '+' (reduce remaining)
            take_plus = dfs(i + 1, remaining - nums[i])

            # Choose '-' (increase remaining)
            take_minus = dfs(i + 1, remaining + nums[i])

            return take_plus + take_minus

        return dfs(0, target)
