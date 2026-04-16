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

# wrapper helper function => why it is needed

# end se jump karu aur 1 step jump karu => 1 step jump kia + jump krne ka cost add kr du 
# end se jump karu aur 2 step jump karu => 2 step jump kia + jump krne ka cost add kr du

# minimum cost to reach the top of the staircase => minimum lia (1 step jump kia, 2 step jump lia)

# =================================

# base case
# You may choose to start at the index 0 or the index 1 floor.
# n = 0 => cost 0 => base case
# n = 1  => cose 0 => base case
# n = 2  =>  cost is not zero => not base case
