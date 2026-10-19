class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])

        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r, c, visited):
            # Reverse flow: start at the ocean and climb to equal/higher cells
            visited[r][c] = True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if not visited[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)

        # Pacific: top row + left column
        for c in range(n):
            dfs(0, c, pac)
        for r in range(m):
            dfs(r, 0, pac)

        # Atlantic: bottom row + right column
        for c in range(n):
            dfs(m - 1, c, atl)
        for r in range(m):
            dfs(r, n - 1, atl)

        return [[r, c] for r in range(m) for c in range(n) if pac[r][c] and atl[r][c]]