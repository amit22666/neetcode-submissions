class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # At least one element exists
        ans = nums[0]
        
        # Prefix pass (left to right)
        prefix = 1
        for x in nums:
            prefix *= x
            ans = max(ans, prefix)
            if prefix == 0:
                prefix = 1  # reset after zero
            print(ans)
        
        # TO HANLE NEGATIVE SCENARIO WE NEED SUFFIX PRODUCT





        

        # # Suffix pass (right to left)
        suffix = 1
        for x in reversed(nums):
            suffix *= x
            ans = max(ans, suffix)
            if suffix == 0:
                suffix = 1  # reset after zero
        
        return ans
