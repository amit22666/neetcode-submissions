class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        def dfs(r, c):
            # Out of bounds or water or already visited → stop
            if (
                r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                grid[r][c] == '0' or 
                (r, c) in visited
            ):
                return
            
            visited.add((r, c))     # mark this land as visited
            
            # explore neighbors (spread out on the island)
            dfs(r+1, c)   # down
            dfs(r-1, c)   # up
            dfs(r, c+1)   # right
            dfs(r, c-1)   # left

        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    islands += 1     # new island discovered
                    dfs(r, c)        # paint the whole island
        
        return islands