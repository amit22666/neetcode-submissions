import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        n = len(s)

        # 🚨 feasibility check
        if max(freq.values()) > (n + 1) // 2:
            return ""

        # max heap (-count, char)
        heap = [(-cnt, ch) for ch, cnt in freq.items()]
        heapq.heapify(heap)

        res = []
        prev_cnt, prev_ch = 0, ""

        while heap:
            cnt, ch = heapq.heappop(heap)
            res.append(ch) 
            cnt += 1  # (cnt - 1) since cnt is negative. we have to add

            # first iteration it will be 0. push previous back if still remaining
            if prev_cnt != 0:
                heapq.heappush(heap, (prev_cnt, prev_ch))

            
            prev_cnt, prev_ch = cnt, ch

        return "".join(res)
