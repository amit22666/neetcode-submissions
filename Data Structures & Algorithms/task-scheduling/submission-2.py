# https://chatgpt.com/share/68d7a997-aab4-8009-9a6f-08ae8b8cdc31

# AAA BB CC
# C B C B A _ A _ A <- not efficient
# take the task which require more cpu cycle or which has max frequency
# A B A C A B C

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
                # we are executing this task. 
                # pop the element with max count/frequency. so we use maxHeap
                taskCount = heapq.heappop(maxHeap)
                cnt = taskCount + 1 # (taskCount - 1) decrement count (-ve so adding it)
                if cnt:
                    # time +n is the next time we have execute this task
                    q.append([cnt, time + n])  
            if q and q[0][1] == time:
                # this task becomes candidate to execute
                CandidateElement = q.popleft()[0]
                heapq.heappush(maxHeap, CandidateElement)
        return time
