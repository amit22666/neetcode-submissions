class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        
        # 1) Collect all rotten fruits and count fresh ones
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        # If no fresh fruits, return 0 immediately
        if fresh == 0:
            return 0
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = -1
        
        # 2) BFS: spread rot level by level
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1
        
        # 3) Check if all fresh fruits rotted
        return minutes if fresh == 0 else -1
