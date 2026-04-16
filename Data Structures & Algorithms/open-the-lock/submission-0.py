
from collections import deque
from typing import List, Set

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        BFS over lock states:
        - Nodes: 4-digit strings (e.g., "0123")
        - Edges: change one digit by +1 or -1 (wrap-around)
        - Blocked: any state in deadends
        - Goal: shortest number of moves from "0000" to target
        """
        dead: Set[str] = set(deadends)
        
        start = "0000"
        if start in dead:
            return -1
        if target == start:
            return 0
        
        # Helper: generate all neighbors by turning one wheel up/down
        def neighbors(s: str):
            for i in range(4):
                d = int(s[i])
                # Turn wheel i one step up (wrap 9 -> 0)
                up = (d + 1) % 10
                # Turn wheel i one step down (wrap 0 -> 9)
                down = (d - 1) % 10
                yield s[:i] + str(up) + s[i+1:]
                yield s[:i] + str(down) + s[i+1:]
        
        # Standard BFS
        q = deque([start])
        visited = {start}
        moves = 0
        
        while q:
            # Process one BFS level (all states at current distance)
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return moves
                # Try all 8 neighbors (2 per wheel × 4 wheels)
                for nxt in neighbors(cur):
                    if nxt not in visited and nxt not in dead:
                        visited.add(nxt)
                        q.append(nxt)
            moves += 1
        
        # If BFS finishes without finding target, it's impossible
        return -1
