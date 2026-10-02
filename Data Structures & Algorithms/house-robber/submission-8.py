class Solution:
    def rob(self, nums):
        memo = {}

        def dfs(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            rob_current = nums[i] + dfs(i + 2)
            skip_current = dfs(i + 1)

            memo[i] = max(rob_current, skip_current)
            return memo[i]

        return dfs(0)