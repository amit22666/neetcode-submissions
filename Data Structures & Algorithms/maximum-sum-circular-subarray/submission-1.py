class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #Reverse of Kadane algorithm - minimum subarray sum
        # 5, -3 , 5 
        globalMin = nums[0]
        curMin = 0
        globalMax = nums[0]
        curMax = 0

        total = 0
        for num in nums:
            total = total + num

            curMin = min(curMin + num, num)
            globalMin = min(curMin, globalMin)

            curMax = max(curMax+num, num)
            globalMax = max(globalMax, curMax)
        # nums=[-2,-3,-1]
        return max(total-globalMin, globalMax) if globalMax > 0 else globalMax