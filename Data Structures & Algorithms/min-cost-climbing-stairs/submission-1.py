class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(n: int) -> int:
            # Base case: if n <= 1, no cost
            if n <= 1:
                return 0
            
            # Store recursive answers in variables
            cost_from_n1 = cost[n - 1] + helper(n - 1)
            cost_from_n2 = cost[n - 2] + helper(n - 2)
            
            # Compute result for current n
            result = min(cost_from_n1, cost_from_n2)
            return result
        
        # Start from the top (len(cost))
        ans = helper(len(cost))
        return ans

# end se jump karu toh 1st step pr aane ka cost
# end se jump karu toh 2nd step pr aane ka cost
# undono ka minimum mera answer

# =================================


