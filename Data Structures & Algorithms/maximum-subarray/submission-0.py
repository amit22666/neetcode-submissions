class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0 # if array starts with -ve number
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum = curSum + num
            maxSum = max(curSum,maxSum)
        return maxSum