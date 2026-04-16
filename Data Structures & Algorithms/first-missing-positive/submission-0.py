class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # -ve means that value is present in the array

        # handle -ve value first -> to make our algo work
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1  # made -ve to positive

            
        for i in range(n):
            if 0 <= abs(nums[i]) - 1 < n:
                val = abs(nums[i])  - 1
                if nums[val] > 0:
                    nums[val] = nums[val] * -1

        for i in range(n):
            if nums[i] > 0:
                return i+1

        return n+1

        