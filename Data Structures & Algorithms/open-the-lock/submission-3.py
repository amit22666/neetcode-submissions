from collections import deque

class Solution:
    def openLock(self, deadends, target):
        dead = set(deadends)
        if "0000" in dead:
            return -1
        
        def neighbors(code):
            res = []
            for i in range(4):
                digit = int(code[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_code = code[:i] + str(new_digit) + code[i+1:]
                    res.append(new_code)
            return res
        
        q = deque([("0000", 0)])
        visited = set(["0000"])
        
        while q:
            code, steps = q.popleft()
            if code == target:
                return steps
            
            for nxt in neighbors(code):
                if nxt not in visited and nxt not in dead:
                    visited.add(nxt)
                    q.append((nxt, steps + 1))
        
        return -1
