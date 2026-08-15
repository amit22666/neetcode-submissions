class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        aCount = a
        bCount = b
        cCount = c
        maxHeap = []
        # negative because maxHeap
        # a is a ka count that is given as input param
        for count, char in [(-aCount, "a"), (-bCount, "b"), (-cCount, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            # previous 2 same character ka check
            # len(res) > 1 , atleat 2 characters hai?
            # last 2 character same hai?
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap: 
                    break # break imp
                # pop second most common/frequent character
                count2, char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1 # decrement the count2 - 1 (since it is a max heap and count are negative so we have added 1)

                # if count exist then add 2nd MFC character to max heap
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
            else:
                res += char
                count += 1 # decrement the count - 1 (since it is a max heap and count are negative so we have added 1)
            if count:
                heapq.heappush(maxHeap, (count, char))

        return res