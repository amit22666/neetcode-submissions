class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # based on previous relationship we want to take current index decision
        # previous relationship is stored in prev -> '>' or '<'
        # if current condition mis-matches with prev sign then it is terbulant

# since we have find range (ie.) subarray length we can use sliding window. and is our answer longest window
        l, r, res, prev = 0, 1, 1, ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""

        return res

        