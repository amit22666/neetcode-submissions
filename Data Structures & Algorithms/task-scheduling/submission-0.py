class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-1*cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() #pair of [-cnt,idleTime]
        while maxHeap or q:
            time = time + 1
            if not maxHeap:
                time = q[0][1]
            else:
                taskCount = heapq.heappop(maxHeap)
                cnt = taskCount + 1 # decrement count (-ve so adding it)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
