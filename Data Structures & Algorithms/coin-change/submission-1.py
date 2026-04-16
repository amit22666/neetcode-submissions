class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(rem):
            # If exact amount reached
            if rem == 0:
                return 0

            # If we overshoot
            if rem < 0:
                return float('inf')

            if rem in memo:
                return memo[rem]

            # Try every coin
            ans = float('inf')
            for c in coins:
                res = dfs(rem - c)
                if res != float('inf'):
                    ans = min(ans, 1 + res)

            memo[rem] = ans
            return ans
        
        result = dfs(amount)
        return -1 if result == float('inf') else result
