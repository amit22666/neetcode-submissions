class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Step 1: Define a function that takes nums (list of integers) and target (integer) as input

        # Step 2: Create an empty dictionary (hashmap) to store numbers we have seen
        # The key will be the number, and the value will be its index
        seen_nums = {}

        # Step 3: Loop through nums with both index and value (use enumerate)
        for idx, num in enumerate(nums):

            # Step 3.1: For the current number, calculate the complement (target - current number)
            remaining_half = target - num

            # Step 3.2: Check if the complement is already in the dictionary
            if remaining_half in seen_nums:
                # Step 3.2.1: If yes, return [index of complement from dictionary, current index]
                # (this ensures smaller index comes first)
                return [seen_nums[remaining_half], idx]

            # Step 3.3: If complement is not found, store the current number with its index in the dictionary
            seen_nums[num] = idx

        # Step 4: (This line won’t really be reached because the problem guarantees a solution)
        return [0,0]
