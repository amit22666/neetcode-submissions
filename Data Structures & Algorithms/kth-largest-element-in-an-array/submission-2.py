class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k #shurwat se len(nums) - k pr le aaya aur uuse chote element left mein kr die

    # partitioning

        def quickSelect(l,r):
            pivot, p = nums[r], l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums [i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k: # left side 
                return quickSelect(l,p-1)
            elif p <k : # right side
                return quickSelect(p+1,r)
            else: # p == k
                return nums[p]
        return quickSelect(0,len(nums) - 1)
        