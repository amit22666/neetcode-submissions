class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Step 1: Define a function that accepts one parameter named nums

# Step 2: Calculate the length of nums and store it in a variable n
        lenOfNums = len(nums)
        n = lenOfNums

# Step 3: Create a new list named ans with size equal to 2 * n
        ans = list(range(n*2))

# Step 4: Start a loop iterating i from 0 to n - 1
        for i in range(n):

# Step 4.1: Set ans[i] equal to nums[i] to copy the first half
            ans[i] = nums[i]

# Step 4.2: Set ans[i + n] equal to nums[i] to copy the second half
            ans[i+n] = nums[i]

# Step 5: After the loop, return the list ans
        return ans

# Step 6: Test your function using the provided examples to verify output
