class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(i: int) -> int:
            # Base case: past the last step
            if i >= len(cost):
                return 0
            
            # Store recursive answers in variables
            cost_one_step = helper(i + 1)
            cost_two_steps = helper(i + 2)
            
            # Compute result for current step
            result = cost[i] + min(cost_one_step, cost_two_steps)
            return result
        
        # Final answer: choose starting from step 0 or step 1
        ans = min(helper(0), helper(1))
        return ans
