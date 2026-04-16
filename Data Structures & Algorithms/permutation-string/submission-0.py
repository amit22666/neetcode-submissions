class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # approach 1 - compare 2 hash maps
        
        if len(s2) < len(s1):
            return False   # can't fit s1 into s2

        s1FreqMap = Counter(s1)
        s2FreqMap = Counter()

        l = 0
        for r in range(len(s2)):
            # expand window
            s2FreqMap[s2[r]] += 1

            # shrink window if size exceeds s1
            if r - l + 1 > len(s1):
                s2FreqMap[s2[l]] -= 1
                if s2FreqMap[s2[l]] == 0:
                    del s2FreqMap[s2[l]]
                l += 1

            # compare maps when window size == len(s1)
            if s1FreqMap == s2FreqMap:
                return True

        return False
