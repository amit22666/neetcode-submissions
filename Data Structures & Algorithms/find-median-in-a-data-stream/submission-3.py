class MedianFinder:

    def __init__(self):
        # heap list 
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        # first add element to min/max heap -> due to this 2 problems comes into picture.
        # if self.small and num < self.small[0]:
        #     heapq.heappush(self.small, (-1)*num)
        # else:
        #     heapq.heappush(self.large, num)
        
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num) # (right side) min heap
        else:
            heapq.heappush(self.small, -1 * num) # (left side) max heap
            
        # min heap -1 multiply
        # 2 problems
        # -> first part of the heap might have bigger elements than 2nd part of the heap

        #  -> first part of the heap might have more elements than 2nd part of the heap
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, (-1)*val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0     
        