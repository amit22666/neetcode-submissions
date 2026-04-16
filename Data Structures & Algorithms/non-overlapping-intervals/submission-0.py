class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        startTime = 0
        endTime = 1
        res = 0
        intervals.sort()
        prevEnd = intervals[0][endTime]
        for start, end in intervals[1:]:
            if start >= prevEnd: # non-overlapping interval important prevEnd not end
                prevEnd = end
            else:
                # all other are overlapping condition
                res = res + 1
                prevEnd = min(end,prevEnd)
        return res 
        