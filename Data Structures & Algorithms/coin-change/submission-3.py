from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remainingAmount):
            if remainingAmount == 0:
                return 0
            if remainingAmount < 0:
                return float('inf')

            if remainingAmount in memo:
                return memo[remainingAmount]

            minCoins = float('inf')
            for coin in coins:
                res = dfs(remainingAmount - coin)
                if res != float('inf'):
                    minCoins = min(minCoins, res + 1)

            memo[remainingAmount] = minCoins
            return minCoins

        result = dfs(amount)
        return -1 if result == float('inf') else result