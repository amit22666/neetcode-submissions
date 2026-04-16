class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        perms = [[]]
        for n in nums: # iterate over given num
            new_perms = []
            for p in perms: # insert n in every permuatation
                # print("len(p) = ", len(p)+1)
                for i in range(len(p) + 1): # insert n at all index
                    p_copy = p.copy()
                    # print("i (index), n (value)  = ", i, n)
                    p_copy.insert(i,n) # insert n at ith position
                    # print("p_copy = ", p_copy)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms
