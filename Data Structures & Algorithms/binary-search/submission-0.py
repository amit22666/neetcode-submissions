class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Step 1: Define a function that takes nums (sorted list of integers) and target (integer) as input

        # Step 2: Initialize two pointers:
        # left = 0 (start of the list), right = len(nums) - 1 (end of the list)
        left = 0
        right = len(nums) - 1

        # Step 3: While left is less than or equal to right
        while left <= right:
            # Step 3.1: Find the middle index = (left + right) // 2
            mid = (left + right) // 2
            # Step 3.2: Get the middle element = nums[middle]
            if nums[mid] == target:
                return mid
            # Step 3.3: If middle element == target
                # Return middle (because we found the target)
            if nums[mid] < target:
                left = mid + 1

            # Step 3.4: If middle element < target
                # Move the left pointer to middle + 1 (search in right half)

            # Step 3.5: Else (middle element > target)
                # Move the right pointer to middle - 1 (search in left half)
            else:
                right = mid - 1

        # Step 4: If loop ends without finding target, return -1
        return -1

        