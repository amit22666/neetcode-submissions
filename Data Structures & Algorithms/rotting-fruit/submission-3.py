class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        q = deque()

        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:  # rotten orrange identifier
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1 # to check in end all the fresh oranges are rotten
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        if fresh == 0:
            return 0

        minutes = -1
        while q:
            minutes = minutes + 1
            for i in range(len(q)):
                r,c = q.popleft()
                for dr , dc in directions:
                    nr = r + dr
                    nc = c + dc
                    # out of bound condition
                    if 0<=nr< ROWS and 0<=nc<COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))

        return minutes if fresh == 0 else -1
        