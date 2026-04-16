from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1

        # shrink window until only k elements remain
        while r - l + 1 > k:
            # compare which side is farther from x
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1

        return arr[l:r+1]
