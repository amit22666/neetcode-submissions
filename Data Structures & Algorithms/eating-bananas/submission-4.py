# sticky notes
# main door -> life sorted -> big paper
    # weekend list
    # healthy list -> ABC JUICE, leftover
# second door knowledge sorted -> sticky notes

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # binary serach template
        # define search space
        # iterate over it l<=r or true
        # movement left or right
        # found target

        l = 1
        r = max(piles)
        res = r

        while l <= r:
            speed = (l+r)//2 # speed -> itne bananas khaegi
            time = 0
            for pile in piles: # pile ko khane mein kitna time lga
                time += math.ceil((float(pile)/speed))
            
            if time <= h:
                res = min(speed, res)
                r = speed - 1
            else:
                l = speed + 1
        return res
                



        

            
            