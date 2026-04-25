"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # confict happen -> increase room count

        startTime = sorted([interval.start for interval in intervals])
        endTime = sorted([interval.end for interval in intervals])

        start = 0
        end = 0

        count = 0
        maxDays = 0


        while start < len(intervals):
            if endTime[end] > startTime[start]:
                count += 1
                start += 1
            else:
                end += 1
                # meeting ended so room got free
                count += -1 
            maxDays = max(maxDays,count)

        return maxDays