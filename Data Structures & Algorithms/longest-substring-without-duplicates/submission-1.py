class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # window with distict character
        # if character repeats in the window.
        # Then from left short the window

        charSet = set()
        l = 0
        res = 0
        # expanding window via loop
        for r in range(len(s)): # r < n
            # shrink window
            while s[r] in charSet:
                charSet.remove(s[l])
                l = l + 1
            # len of window = r-l+1
            res = max(res,r-l+1)
            charSet.add(s[r])
            
        return res