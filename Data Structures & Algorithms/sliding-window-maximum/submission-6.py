class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ngl. - stDeque, ack -
        # k - window size maintain

        # observation - 1
        # piche deletion
        # aage insertion

            # observation - 2
        # new element in window > already present hai winodow mein
        # already present hai winodow mein <- kabhi answer nhi honge
            # -> piche wale element go maintain nhi krna

        l = 0
        r = 0
        arr = nums
        dq = deque() # top -> max element 
        res = []

        for r in range(len(arr)):
            
            while dq and arr[dq[-1]] <= arr[r]:
                dq.pop()

            
            dq.append(r) # 0 1 2 3 
            # print("l ", l)
            # print("r ", r)
            # print("dq ", dq[0])

            # print("window size", r-l+1)
            if r-l+1 > k:
                # print("increment l")
                l = l + 1
            
            if dq[0] < l: # l = 0 = 1
                # out of window
                dq.popleft()

            

            if r-l+1 == k:
                print("answer ", dq[0])
                res.append(arr[dq[0]])
            

        return res



        