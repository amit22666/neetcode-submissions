class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # check for overlapping condition
            endTime = 1
            startTime = 0
            if newInterval[endTime] < intervals[i][startTime]:
                # Inserted with No overlapping, we got answer here 
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[startTime] > intervals[i][endTime]:
                # No overlapping now , might overlap in future
                res.append(intervals[i])
            else:
                # overlapping happened
                newInterval = [
                    min(newInterval[startTime], intervals[i][startTime]),
                    max(newInterval[endTime], intervals[i][endTime])
                ]
        res.append(newInterval)
        return res