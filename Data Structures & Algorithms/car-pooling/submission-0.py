class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # O (n logn) . it can be optimized to O (n)
        # see video  take array of [0] * 1001. constraint
        trips.sort(key=lambda t: t[1])
        # which trip is getting completed we will get to know from min heap . (from end we will get to know)
        minHeap = []  # pair of [end, numPassengers]
        curPass = 0

        for numPass, start, end in trips:
            # first iteration while loop will not run
            #  is any previous trip completed?
            while minHeap and minHeap[0][0] <= start:
                droppedPassangers = heapq.heappop(minHeap)[1]
                curPass -= droppedPassangers

            curPass += numPass
            if curPass > capacity:
                return False

            heapq.heappush(minHeap, [end, numPass])

        return True