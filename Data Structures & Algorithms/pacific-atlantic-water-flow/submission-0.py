
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Edge case: empty grid
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        # Two visitation matrices:
        # pac[r][c] = True if cell (r,c) can reach the Pacific (top/left)
        # atl[r][c] = True if cell (r,c) can reach the Atlantic (bottom/right)
        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]
        
        # Directions for moving up, down, left, right
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r: int, c: int, seen: List[List[bool]]) -> None:
            """
            Reverse-flow DFS:
            Start from an ocean border and move into the island.
            We can only move to neighbors with height >= current height,
            because in the original problem water flows from high to low.
            So reversing means we 'climb' to equal/higher neighbors.
            """
            seen[r][c] = True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # Check bounds
                if 0 <= nr < m and 0 <= nc < n:
                    # If not visited and neighbor is equal/higher,
                    # it means water from neighbor can flow down to (r,c),
                    # hence neighbor can reach this ocean.
                    if not seen[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, seen)
        
        # --- Pacific: top row and left column ---
        # Top row (row = 0)
        for c in range(n):
            dfs(0, c, pac)
        # Left column (col = 0)
        for r in range(m):
            dfs(r, 0, pac)
        
        # --- Atlantic: bottom row and right column ---
        # Bottom row (row = m - 1)
        for c in range(n):
            dfs(m - 1, c, atl)
        # Right column (col = n - 1)
        for r in range(m):
            dfs(r, n - 1, atl)
        
        # Collect cells that can reach both oceans
        result = []
        for r in range(m):
            for c in range(n):
                if pac[r][c] and atl[r][c]:
                    result.append([r, c])
        
        return result
