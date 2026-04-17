class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # socho -> nge -> window size tak -> stack
        # window ko move kro -> piche se element delete krna hai
        # iss lie stack ki jagah deque use kr rhe hai


        dq = deque()
        l = 0
        res = []
        arr = nums
        for r in range(len(arr)):
            
            while dq and arr[dq[-1]] <= arr[r]:
                dq.pop()
            
            dq.append(r) # index


            
            if r - l + 1 > k:
                l += 1

            if dq[0] < l:
                dq.popleft()


            if r-l+1 == k:
                res.append(arr[dq[0]])

        return res