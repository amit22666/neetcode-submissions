class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Boyer–Moore Voting Algorithm solves it in O(n) time and O(1) space.
        # Step 1: Define a function that accepts nums (a list of integers)

        # Step 2: Initialize two variables:
        #         candidate = None (to store the potential majority element)
        #         count = 0 (to track how many times candidate is supported)
        candidate = 0
        count = 0

        # Step 3: Loop through each number in nums
        for num in nums:
            # Step 3.1: If count is 0, set candidate to the current number
            if count == 0:
                candidate = num
            # Step 3.2: If the current number is equal to candidate, increment count
            if  num == candidate:
                count = count + 1
            # Step 3.3: Otherwise, decrement count
            else:
                count = count - 1
        # Step 4: After finishing the loop, candidate will hold the majority element

        # Step 5: Return candidate
        return candidate
