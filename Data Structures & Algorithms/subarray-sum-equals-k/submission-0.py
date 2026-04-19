class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # prefix[r] - prefix[l] = k # 1 found subarray
        # prefix[r] - k = prefix[l] # count subarray which follow this.
        # Then they will have subarray sum equal to k

        
        countTillR = 0
        arr = nums
        prefixSumR = 0
        freqMap = {0: 1}
        for r in range(len(arr)):
            prefixSumR += arr[r]
            countTillR += freqMap.get(prefixSumR - k,0)
            freqMap[prefixSumR] =  freqMap.get(prefixSumR,0) + 1
            
        
        return countTillR