class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Step 1: Define a function that takes an array of integers (nums) as input

        # Step 2: Create an empty set to keep track of numbers we have already seen
        empty_set = set()


        # Step 3: Loop through each number in nums one by one
        for element in nums:

            # Step 3.1: For the current number, check if it is already in the set
            if element in empty_set:

                # Step 3.1.1: If it is in the set, return True (because we found a duplicate)
                return True
            
            # Step 3.2: If it is not in the set, add this number to the set
            empty_set.add(element)
        # Step 4: After finishing the loop, return False (because no duplicates were found)
        return False