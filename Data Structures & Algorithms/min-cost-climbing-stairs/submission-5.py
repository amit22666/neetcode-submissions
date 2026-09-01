# POINT TO NOTE -> top of the staircase is n + 1 not n

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def helper(i):

            # basecase
            if i<=1:
                return 0

            if i in memo:
                return memo[i]

            oneStepMinCost = cost[i-1] + helper(i-1) # 1 step cost
            twoStepMinCost = cost[i-2] + helper(i-2) # 2 step cost

            memo[i] = min(oneStepMinCost,twoStepMinCost)
            return memo[i]
        return helper(len(cost))