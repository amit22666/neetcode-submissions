# tasks = [[5,2],[4,4],[4,1],[2,1],[3,3]]
# Output: [3,4,2,0,1]

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
            print(t)
        # t = [0,1,2,3,4]
        # sort task via enque time, 
        # pick the min processing time task
        tasks.sort(key=lambda t:t[0])
        minHeap = []
        res=[]
        i = 0
        time = tasks[0][0]
        while i < len(tasks) or minHeap:
            while i < len(tasks) and tasks[i][0]<=time:
                heapq.heappush(minHeap, (tasks[i][1],tasks[i][2]))
                i = i + 1
            if not minHeap:
                time = tasks[i][0]
            else:
                procTime, index = heapq.heappop(minHeap)
                time += procTime
                res.append(index)
        return res

        