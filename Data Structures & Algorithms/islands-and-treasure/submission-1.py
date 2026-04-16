class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Modify the grid in-place:
          -1 : water (blocked)
           0 : treasure
         INF : land (to fill with distance to nearest treasure)
        """
        if not grid or not grid[0]:
            return
        
        m, n = len(grid), len(grid[0])
        INF = 2**31 - 1
        
        q = deque()

        # 1) Add all treasure cells to the queue (multi-source BFS).
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))

        # 2) BFS to fill nearest distance to treasure for INF cells.
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # valid cell and unvisited land (INF)
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1  # distance from nearest treasure
                    q.append((nr, nc))
