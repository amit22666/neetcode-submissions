class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r,c):
            # dfs in all direction

            # out of bound condition

            # zero value condition

            # visited condition

            if (r < 0 or r == ROWS or c < 0 or
                c == COLS or grid[r][c] == 0 or
                (r, c) in visit
            ):
                return 0

            visit.add((r,c))

            # dfs call
            localArea = 1 + dfs(r+1,c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r,c-1)
            return localArea

        area = 0
        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    area = dfs(i,j)
                    maxArea = max(maxArea, area)
        return maxArea
        