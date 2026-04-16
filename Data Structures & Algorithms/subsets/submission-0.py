class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i>= len(nums):
                res.append(subset.copy())
                return
            # choice diagram
            subset.append(nums[i]) # pick
            dfs(i+1)
            subset.pop() # not pick
            dfs(i+1)
        dfs(0)
        return res
        