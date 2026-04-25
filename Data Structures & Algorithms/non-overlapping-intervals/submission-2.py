class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        startTime = 0
        endTime = 1
        count = 0
        intervals.sort()
        prevEnd = intervals[0][endTime]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                # non-overlapped
                prevEnd = end
            else:
                count += 1
                prevEnd = min(end,prevEnd)

        return count
        