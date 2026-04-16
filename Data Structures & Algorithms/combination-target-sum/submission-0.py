class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            dfs(i,cur,total+nums[i]) # unbounded knapsak -> pick
            cur.pop()
            dfs(i+1,cur, total) # not pick

        dfs(0,[],0)
        return res
        