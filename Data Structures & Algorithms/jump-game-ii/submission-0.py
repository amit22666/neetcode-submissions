class Solution:
    def jump(self, nums: List[int]) -> int:

        # window -> (l, maxJump)
        # max jump = max value in that window
        jump = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest,nums[i]+i)
            l = r + 1
            r = farthest
            jump += 1
        return jump
            


        