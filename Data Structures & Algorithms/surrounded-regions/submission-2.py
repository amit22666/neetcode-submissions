class Solution:
    def solve(self, board):
        if not board:
            return
        
        rows, cols = len(board), len(board[0])
        
        # DFS to mark safe O's
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if board[r][c] != 'O':
                return
            
            board[r][c] = 'B'  # Mark as safe
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        # 1️⃣ Mark all border O's with B
        for i in range(rows): # mark all assotiated O with X for that cell
            if board[i][0] == 'O': dfs(i, 0) # first col
            if board[i][cols-1] == 'O': dfs(i, cols-1) # last col
        
        for j in range(cols):
            if board[0][j] == 'O': dfs(0, j) # first row
            if board[rows-1][j] == 'O': dfs(rows-1, j) # last row

        #===========================
        
        # 2️⃣ Convert all remaining O → X (they are surrounded)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        # 3️⃣ Convert all B → O (safe regions)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'B':
                    board[i][j] = 'O'
