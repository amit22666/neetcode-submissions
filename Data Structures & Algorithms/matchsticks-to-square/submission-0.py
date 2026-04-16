class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # recursion is different from other backtracking problems
        # we try to place stick and do it 4 time
        # if we are not able to do it. Try all 4 side. then return False
        
        length = sum(matchsticks)//4
        side = [0] * 4
        if sum(matchsticks)/4 != length:
            return False

        matchsticks.sort(reverse=True)
        # traverse array by index i
        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            # expore all 4 sides/path
            for j in range(4):
                if side[j] + matchsticks[i] <= length:
                    side[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    # explored this path now remove this matchstick
                    side[j] -= matchsticks[i]
            return False

        return backtrack(0)
