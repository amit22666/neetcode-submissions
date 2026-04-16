class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # visited set
        visit = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i,j):
            if i< 0 or j<0 or i>=rows or j>=cols:
                return 1
            if grid[i][j] == 0: #water
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            perimeter =  dfs(i-1,j) + dfs(i,j-1) + dfs(i+1,j) + dfs(i,j+1)
            return perimeter
            
        # we have to iterate on all the cell as we don't know which cell is 1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1: # block 
                    return dfs(i,j) 
    # since return is here, after first dfs call. 
    # Return will be called and loop will exited
        return 0