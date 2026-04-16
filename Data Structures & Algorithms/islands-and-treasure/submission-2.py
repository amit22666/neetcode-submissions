class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        if not grid or not grid[0]:
            return

        ROWS, COLS = len(grid), len(grid[0])
        INF = 2**31 - 1

        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                # if neighbour valid
                if 0<=nr<ROWS and 0<= nc < COLS and grid[nr][nc] == INF: # LAND 
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))


        

        