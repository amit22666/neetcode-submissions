class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Input: nums = [1,2,1]
        # Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
        
        # pick or do not pick


        #================

        # result array
        res = []
        nums.sort()

        # nums sort
        # why to sort number -> to skip duplicates easily

        def backtrack(i,subset):
            # we reached end of input array
            if i == len(nums):
                res.append(subset[::]) # [:] To create copy of subset
                return

            # include
            subset.append(nums[i])
            backtrack(i+1,subset)
            subset.pop()
            # do not include
            # skip duplicate
            while i+1 <len(nums) and nums[i] == nums[i+1]:
                i = i+1
            backtrack(i+1,subset)
        backtrack(0,[]) 

        return res



        # backtrack(0,[])

# if i equal to len of nums -> found subset -> append
# All subset that include num[i]
    # append
    # backtrack
    # pop

# All subset that don't include nums[i]
    # skip all duplicates

    # backtrack

    # return res


