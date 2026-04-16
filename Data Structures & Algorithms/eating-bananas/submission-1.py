class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min speed -> so that we can finish banana under k

        # speed ki range
        # 1 to max(piles)
        # max(piles) speed indicate. every pile can be eaten in 1 unit time
        # now even if we increase speed this time cannot be reduced

        l = 1
        r = max(piles)
        res = r
        
        while l <= r:
            time = 0
            speed = (l+r)//2
            for pile in piles:
                time +=  math.ceil(float(pile)/speed)

            if time <= h:
                res = speed
                r = speed - 1
            else:
                l = speed + 1

        return res
            