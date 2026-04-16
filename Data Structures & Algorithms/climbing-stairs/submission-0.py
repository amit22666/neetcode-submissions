class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n == 0 or n == 1:
            return 1
        OneStepWays = self.climbStairs(n - 1)
        TwoStepWays = self.climbStairs(n - 2)
        # Recursive calls
        return OneStepWays + TwoStepWays