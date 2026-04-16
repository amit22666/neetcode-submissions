"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTime = sorted([i.start for i in intervals])
        endTime = sorted([i.end for i in intervals])
        s = e = 0 #two pointer
        res = count = 0
        while s < len(intervals):
            if startTime[s] < endTime[e]: # overlapping condition
                s = s + 1
                count = count + 1 # no of meeting room
            else: # non-overlapping
                e = e + 1
                count = count - 1
            res = max(res, count)
        return res