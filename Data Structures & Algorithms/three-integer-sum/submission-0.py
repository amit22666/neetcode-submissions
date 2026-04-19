class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            # skip duplicate i
            if i > 0 and nums[i] == nums[i-1]: # forgot
                continue

            l, r = i + 1, n - 1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicate l
                    while l < r and nums[l] == nums[l-1]: # forgot duplicate
                        l += 1
                    # skip duplicate r
                    while l < r and nums[r] == nums[r+1]: # forgot duplicate
                        r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    r -= 1

        return res


        