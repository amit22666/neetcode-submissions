from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        tFreq = Counter(t)
        windowFreq = Counter()
        l = 0
        res, resLen = [-1, -1], float('inf')

        for r in range(len(s)):
            windowFreq[s[r]] += 1

            # shrink window when valid
            while all(windowFreq[c] >= tFreq[c] for c in tFreq):
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                windowFreq[s[l]] -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""
