class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, curr_sum):
            # If we've processed all numbers, check if we hit target
            if i == len(nums):
                return 1 if curr_sum == target else 0

            # Choice 1: put a '+' before nums[i]
            add = dfs(i + 1, curr_sum + nums[i])

            # Choice 2: put a '-' before nums[i]
            subtract = dfs(i + 1, curr_sum - nums[i])

            return add + subtract

        return dfs(0, 0)
