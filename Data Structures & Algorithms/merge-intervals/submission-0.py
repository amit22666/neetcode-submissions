class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort based on start time

        # for edge cases put first interval in output
        startTime = 0 
        endTime = 1
        intervals.sort(key=lambda pair: pair[startTime])
        output = [intervals[startTime]]
        for start, end in intervals:
            lastEnd = output[-1][endTime]
            if start <= lastEnd: # overlapping happened
                output[-1][1] = max(lastEnd, end) # merge logic
            else:
                output.append([start,end])

        # interate over intervals - Get start and current end

            # take the lastEnd (EndTime) -> End time of Interval which has biggest startTime 
            # if current interval start time is less than lastEnd (EndTime)
            # take maximum of lastEnd and current end

            # else -> No overlappping
        return output

        