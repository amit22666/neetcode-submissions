class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        arr = heights
        n = len(arr)
        r = n - 1
        ResArea = 0
        while l < r:
            ResArea = max(ResArea, min(arr[l],arr[r]) * (r-l))
            if arr[l]< arr[r]:
                l += 1
            else:
                r -= 1
        return ResArea
        