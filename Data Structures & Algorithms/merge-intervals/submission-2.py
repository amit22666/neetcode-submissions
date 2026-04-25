class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        startTime = 0
        endTime = 1
        intervals.sort(key=lambda pair: pair[startTime])
        output.append(intervals[0])
        for start, end in intervals:
            if start <= output[-1][endTime]:
                # collition ho gya
                output[-1][endTime] = max(output[-1][endTime],end)
            else:
                output.append([start,end])
        return output