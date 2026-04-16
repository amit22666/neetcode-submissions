class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 1, 2, 3, 4, 5 ,6
        # 3, 4, 5, 6, 1, 2
        # 4, 5, 6 ,1 , 2 , 3
        # 5,6,1,2,3,4 -> mid 1 and left is 5 so left is not sorted
        
        # target = 2 
        # mid = idx -> 2 , value -> 5
        # normally Value at mid > target -> blindly move left
        # but here we have to see the leftmost value -> i.e -> 3
        # since 3 is greater than 2 we move to right instread of left

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] == target:
                return mid

            # left is sorted or not
            if nums[l] <= nums[mid]: # means left is sorted
                if nums[l] <=  target < nums[mid]:                
                    r = mid - 1
                else:
                    l = mid + 1
            # right
            else: # right half is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid +1
                else:
                    r = mid -1

        return -1
                