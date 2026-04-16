from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

    def merge_sort(self, nums, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        # Copy the two halves into temporary arrays
        L = nums[left:mid+1]
        R = nums[mid+1:right+1]

        i = j = 0
        k = left

        # Merge two sorted halves
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        # Copy remaining elements of L
        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1

        # Copy remaining elements of R
        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1