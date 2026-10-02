class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        INF = amount + 1
        memo = {}

        def dfs(i, rem):
            if rem == 0:
                return 0
            if rem < 0 or i == len(coins):
                return INF

            if (i, rem) in memo:
                return memo[(i, rem)]

            take = 1 + dfs(i, rem - coins[i])
            skip = dfs(i + 1, rem)

            memo[(i, rem)] = min(take, skip)
            return memo[(i, rem)]

        ans = dfs(0, amount)
        return -1 if ans == INF else ans