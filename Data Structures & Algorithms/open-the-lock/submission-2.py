from collections import deque

class Solution:
    def openLock(self, deadends, target):
        dead = set(deadends)
        start = "0000"

        # if starting itself is blocked
        if start in dead:
            return -1

        # normal BFS setup
        q = deque()
        q.append((start, 0))   # (code, steps)
        visited = {start}

        def get_neighbors(code):
            result = []
            code = list(code)

            for i in range(4):
                digit = int(code[i])

                # move +1
                up = code.copy()
                up[i] = str((digit + 1) % 10)
                result.append("".join(up))

                # move -1
                down = code.copy()
                down[i] = str((digit - 1) % 10)
                result.append("".join(down))

            return result

        # BFS loop
        while q:
            code, steps = q.popleft()

            # found the answer!
            if code == target:
                return steps

            for nxt in get_neighbors(code):
                if nxt not in visited and nxt not in dead:
                    visited.add(nxt)
                    q.append((nxt, steps + 1))

        return -1
