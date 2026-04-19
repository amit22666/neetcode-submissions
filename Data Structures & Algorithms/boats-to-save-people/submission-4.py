class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        arr = people
        n = len(arr)
        r = n - 1
        boat = 0
        arr = sorted(arr)
        while l <= r:        
            if arr[r] + arr[l] <= limit:
                l += 1
                r -= 1
                boat += 1
            else:
                r -= 1
                boat += 1
        return boat
        