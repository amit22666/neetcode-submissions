class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead: Set[str] = set(deadends)

        start = "0000"
        if start in dead:
            return -1

        if start == target:
            return 0
        

        # generate all neighbours by turning wheel up and down , +1, -1
        def neighbours(s: str):
            for i in range(4):
                d = int(s[i])
                up = (d+1)%10
                down = (d-1)%10
                upValue = s[:i] + str(up) + s[i+1:]
                downValue = s[:i] + str(down) + s[i+1:]
                yield upValue
                yield downValue

        q = deque([start])
        visited = {start}
        moves = 0

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return moves
                for nxt in neighbours(cur):
                    if nxt not in visited and nxt not in dead:
                        visited.add(nxt)
                        q.append(nxt)
            moves += 1
        return -1







        