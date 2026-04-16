class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n == 0 or n == 1:
            return 1
        OneStepWays = self.climbStairs(n - 1)
        TwoStepWays = self.climbStairs(n - 2)
        # Recursive calls
        return OneStepWays + TwoStepWays

        # recursion --> from n to 0
        # You can climb with either 1 ====> means no. of ways to climb stairs if we take 1 step.  => repeat (n-1)
        #  2 steps at a time ===> means no. of ways to climb stairs if we take 2 step  => repeat (n-2)


        # to stop this recursion 
        # base case not given in question , we have to think of it
        # 0 stair -> 1 way => base case
        # 1 stair  -> 1 way => base case
        # 2 stair  -> 2 ways => not base base