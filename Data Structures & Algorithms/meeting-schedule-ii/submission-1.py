"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTime = sorted([interval.start for interval in intervals])
        endTime = sorted([interval.end for interval in intervals])
        s = 0 # two pointer
        e = 0
        day = 0
        maxDays = 0
        while s < len(intervals):
            if endTime[e] > startTime[s]:
                day = day + 1
                s = s + 1
            else:
                e = e + 1
                day = day - 1 # meeting ended so room got free
            maxDays = max(maxDays,day)
        return maxDays

