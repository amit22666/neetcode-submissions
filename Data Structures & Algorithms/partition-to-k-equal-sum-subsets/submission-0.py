# nums = [2,4,1,3,5] k = 3 <- bucket
# [5], [4,1], [3,2]
# 15 / 3 = 5 <- target
# Partition to K subsets = Fill one bucket at a time, never reuse numbers

# We fill one bucket at a time
# Once a bucket reaches target, we start filling the next bucket
# Numbers already used cannot be reused


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) %k:
            return False
        target = sum(nums)/k
        nums.sort(reverse=True)
        used = [False] * len(nums)
        
        def backtrack(i,k,subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0,k-1,0) # everything reset
            for j in range(i,len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j+1,k,subsetSum+nums[j]):
                    return True
                used[j] = False
            return False
        return backtrack(0,k,0)