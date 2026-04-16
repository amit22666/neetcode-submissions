class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # it is graph question
        # dfs we need to do
        rows,cols = len(board), len(board[0])
        visited = set()
        # on the word keep a i var.
        def dfs(r,c, i):
            # new r and new c -> out of bound -> return
            # visited check
            # recursion call in all 4 directions
            if i == len(word):
                return True
            if r<0 or c <0 or r>=rows or c >= cols:
                return False
            if word[i] != board[r][c]:
                return False
            if (r,c) in visited:
                return False
            
            visited.add((r,c))
            res = (dfs(r+1,c,i+1) or
                    dfs(r,c+1,i+1) or
                    dfs(r-1,c,i+1) or
                    dfs(r,c-1,i+1))
            visited.remove((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c, 0):
                    return True
        return False