class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = nums[0]

        cur_max = 1
        cur_min = 1

        for num in nums:
            tmp = cur_max * num

            cur_max = max(num, tmp, cur_min * num)
            cur_min = min(num, tmp, cur_min * num)

            res = max(res, cur_max)

        return res


#         This problem is similar to Kadane's algorithm, but there's a twist:

# A negative × negative = positive
# So the current minimum product can suddenly become the maximum product.

# Therefore, at each position, track:

# Plain Text
# max_prod = maximum product ending at current index
# min_prod = minimum product ending at current index