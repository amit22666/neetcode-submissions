class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            # skip duplicate i
            if i > 0 and nums[i] == nums[i-1]: # forgot
                continue
 
            for j in range(i+1, n):  # forgot
                # skip duplicate j
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                l, r = j+1, n-1
                while l < r:
                    curSum = nums[i] + nums[j] + nums[l] + nums[r]
                    if curSum == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        # skip duplicate l
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        # skip duplicate r
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif curSum < target:
                        l += 1
                    else:
                        r -= 1

        return res
