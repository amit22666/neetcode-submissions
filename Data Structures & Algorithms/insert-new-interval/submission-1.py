class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        startTime = 0
        endTime = 1
        for i in range(len(intervals)):
            if newInterval[endTime] < intervals[i][startTime]:
                # no collision in left side
                res.append(newInterval)
                print("reached here")
                return res + intervals[i:]

            elif newInterval[startTime] > intervals[i][endTime]:
                # no collision in right side, might happen in future
                res.append(intervals[i])
                # res.append(newInterval)
            else:
                # overlapping happend
                newInterval = [
                    min(newInterval[startTime], intervals[i][startTime]),
                    max(newInterval[endTime], intervals[i][endTime])
                ]
                # res.append(newInterval)
        res.append(newInterval)
        return res
            
