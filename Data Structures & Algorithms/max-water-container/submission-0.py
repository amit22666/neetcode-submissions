class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxRes = 0
        while (l < r):
            res = min(heights[r],heights[l])  * (r - l)
            maxRes = max(maxRes, res)
            if heights[l] < heights[r]: # bottle nech
                l += 1
            else:
                r -= 1
        return maxRes


        

        