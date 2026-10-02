class Solution:
    def rob(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob_range(left, right):
            memo = {}

            def dfs(i):
                if i > right:
                    return 0

                if i in memo:
                    return memo[i]

                rob_current = nums[i] + dfs(i + 2)
                skip_current = dfs(i + 1)

                memo[i] = max(rob_current, skip_current)
                return memo[i]

            return dfs(left)

        return max(
            rob_range(0, n - 2),  # exclude last
            rob_range(1, n - 1)   # exclude first
        )