class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2
        memo = {}

        def dfs(i, remaining):
            if remaining == 0:
                return True

            if remaining < 0 or i == len(nums):
                return False

            if (i, remaining) in memo:
                return memo[(i, remaining)]

            memo[(i, remaining)] = (
                dfs(i + 1, remaining - nums[i]) or
                dfs(i + 1, remaining)
            )

            return memo[(i, remaining)]

        return dfs(0, target)