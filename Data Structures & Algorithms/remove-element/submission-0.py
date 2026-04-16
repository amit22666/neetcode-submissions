class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Step 1: Define a function that takes nums (list of integers) and val (integer to remove)

        # Step 2: Create a variable (like k) to keep track of where to place the next valid element
        k = 0

        # Step 3: Loop through each element in nums
        for i in range(len(nums)):
            # Step 3.1: If the current element is not equal to val
            if nums[i] != val:
                # Step 3.1.1: Place this element at index k in nums
                nums[k] = nums[i]
                # Step 3.1.2: Increment k by 1
                k = k+1
        # Step 4: After the loop ends, k will represent the number of elements not equal to val

        # Step 5: Return k as the result
        return k
