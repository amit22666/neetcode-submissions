# POINT TO NOTE -> top of the staircase is n + 1 not n

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def helper(n):

            # basecase
            if n<=1:
                return 0

            if n in memo:
                return memo[n]

            oneStepMinCost = cost[n-1] + helper(n-1) # 1 step cost
            twoStepMinCost = cost[n-2] + helper(n-2) # 2 step cost

            memo[n] = min(oneStepMinCost,twoStepMinCost)
            return memo[n]
        return helper(len(cost))