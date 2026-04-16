class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # -ve means that value is present in the array

        # handle -ve value first -> to make our algo work
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1  # made -ve to positive

            
        for i in range(n):
            if 1 <= abs(nums[i]) <= n:
                NegMarkingIndex = abs(nums[i])  - 1
                if nums[NegMarkingIndex] > 0:
                    nums[NegMarkingIndex] = nums[NegMarkingIndex] * -1

        for i in range(n):
            if nums[i] > 0:
                return i+1

        return n+1

        