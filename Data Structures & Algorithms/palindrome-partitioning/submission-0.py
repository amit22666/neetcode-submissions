class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        # iska tree choice digram ki tarah nhi banta
        # inska tree iterative tarike se banta hai
        def dfs(i):
            if i >= len(s):
                # we found our answer
                # part will contain our answer
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if self.isPali(s,i,j):
                    part.append(s[i:j+1]) # very easy
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res

    def isPali(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l , r = l +1 , r -1
        return True
    