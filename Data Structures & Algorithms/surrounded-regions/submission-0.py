
from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Surrounded Regions (BFS approach)

        Idea:
        - Any 'O' that is connected to the border (top row, bottom row, left col, right col)
          cannot be surrounded by 'X'. We mark all such 'O's as SAFE.
        - After marking, any remaining 'O' must be enclosed by 'X', so flip them to 'X'.
        - Finally, convert all SAFE markers back to 'O'.

        How we mark SAFE:
        - Start BFS from all border 'O's at once (multi-source).
        - While BFS expands, every connected 'O' we visit is marked SAFE ('#').

        Modifies `board` in place.
        """
        # Guard against empty input
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        q = deque()

        def enqueue_if_O(r: int, c: int) -> None:
            """
            If (r, c) is inside the grid and is an 'O', mark it as SAFE ('#')
            and push it into the queue for BFS expansion.

            We mark immediately to avoid revisiting the same cell.
            """
            if 0 <= r < m and 0 <= c < n and board[r][c] == 'O':
                board[r][c] = '#'      # mark as SAFE (connected to border)
                q.append((r, c))       # enqueue for BFS
        
        # ---------------------------------------------------------
        # 1) Seed the BFS with all border 'O's and mark them SAFE.
        #    These are guaranteed to NOT be surrounded.
        # ---------------------------------------------------------

        # Top and bottom rows
        for c in range(n):
            enqueue_if_O(0, c)         # top row
            enqueue_if_O(m - 1, c)     # bottom row

        # Left and right columns
        for r in range(m):
            enqueue_if_O(r, 0)         # left column
            enqueue_if_O(r, n - 1)     # right column
        
        # ---------------------------------------------------------
        # 2) BFS from the borders: mark every 'O' connected to them
        #    as SAFE by turning it into '#'.
        # ---------------------------------------------------------
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 4-directional moves
        while q:
            r, c = q.popleft()
            # Try all 4 neighbors
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                enqueue_if_O(nr, nc)

        # ---------------------------------------------------------
        # 3) Final pass:
        #    - Any remaining 'O' is enclosed -> flip to 'X'.
        #    - Any SAFE '#' should be restored back to 'O'.
        # ---------------------------------------------------------
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # enclosed region -> flip
                elif board[r][c] == '#':
                    board[r][c] = 'O'  # restore SAFE back to 'O'
