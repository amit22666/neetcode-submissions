class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        # If the array is not rotated (already sorted)
        if nums[l] <= nums[r]:
            return nums[l]

        while l <= r:
            # If current window is sorted, the leftmost is the smallest in this window
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])

            # Since line number 12 if false. it means array is rotated
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                # Right half is rotated; min is in left half (including mid)
                r = mid - 1

        return res