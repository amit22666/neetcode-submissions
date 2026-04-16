from collections import Counter
from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        tFreq = Counter(t)
        windowFreq = {}
        have, need = 0, len(tFreq)
        res, resLen = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            c = s[r]
            windowFreq[c] = windowFreq.get(c, 0) + 1

            if c in tFreq and windowFreq[c] == tFreq[c]:
                have += 1

            while have == need:
                # update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # shrink window
                windowFreq[s[l]] -= 1
                if s[l] in tFreq and windowFreq[s[l]] < tFreq[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""
