class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}

        def dfs(num):
            if num == 1:
                return 1

            if num in memo:
                return memo[num]

            res = 0 if num == n else num

            for i in range(1, num):
                res = max(res, dfs(i) * dfs(num - i))

            memo[num] = res
            return res

        return dfs(n)