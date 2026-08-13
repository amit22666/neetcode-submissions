# tasks = [[5,2],[4,4],[4,1],[2,1],[3,3]]
# Output: [3,4,2,0,1]

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
            print(t)
            # [1, 4, 0] # enque time, processing time, index
            # [3, 3, 1]
            # [2, 1, 2]
        tasks.sort(key=lambda t:t[0])
        minHeap = []
        res=[]
        i = 0
        time = tasks[0][0]
        while i < len(tasks) or minHeap: # some task are pending or there are some candidate task
            while i < len(tasks) and tasks[i][0]<=time:
                # task which are not executed and have enque time less then current task
                # add it to heap. As time increases more task becomes candidates
                # from canditates tasks, pick the one which has ((minimum processing time))
                heapq.heappush(minHeap, (tasks[i][1],tasks[i][2]))
                i = i + 1
            if not minHeap: 
                # there is not candidates tasks, increase the time. new task can become candidate
                time = tasks[i][0] # time is increased
            else:
                # from candidate tasks , pick the task with minimum processing time
                # since it is popped from heap it means it is executed
                # increment the time to time + task processing time
                # append the index to answer
                procTime, index = heapq.heappop(minHeap)
                time += procTime
                res.append(index)
        return res

        