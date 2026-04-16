class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0
        r = len(people) - 1
        boat = 0

        while l <= r:
            if limit >= people[l] + people[r]:
                l += 1
                r -= 1
                boat += 1
            else:
                r -=1
                boat += 1
        return boat
        