class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find starting point of sequence
        arr = nums
        arrset = set(arr)
        res = 0
        for r in range(len(arr)):
            if arr[r] - 1 not in arrset:
                # then it is starting point of subsequence
                length = 0
                while arr[r] + length in arrset:
                    length += 1
                res = max(res, length)

        return res