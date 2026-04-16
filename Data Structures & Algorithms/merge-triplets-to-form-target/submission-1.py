class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False
        for t in triplets:
            if t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2]:
                x = True
            if t[0] <= target[0] and t[1] == target[1] and t[2] <= target[2]:
                y= True
            if t[0] <= target[0] and t[1] <= target[1] and t[2] == target[2]:
                z = True
            if x and y and z:
                return True
        return False