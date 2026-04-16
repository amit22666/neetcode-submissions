from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # memo: key = (i, buying), val = max profit from this state

        def dfs(i: int, buying: bool) -> int:
            # Base case: agar days khatam -> profit 0
            if i >= len(prices):
                return 0

            # Memoization: agar pehle compute kiya hai to direct de do
            if (i, buying) in dp:
                return dp[(i, buying)]

            # Option 1: cooldown/skip -> next day same state
            cooldown = dfs(i + 1, buying)

            if buying:
                # Buying state:
                #  - buy karo: paise dene padenge (-prices[i]), next day selling state
                buy = dfs(i + 1, False) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # Selling state:
                #  - sell karo: paise milenge (+prices[i]), aur 1-day cooldown -> i + 2
                sell = dfs(i + 2, True) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        # Start: day 0, buying allowed (haath khaali)
        return dfs(0, True)
