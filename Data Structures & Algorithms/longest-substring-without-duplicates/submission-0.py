class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        l = 0
        r = 0
        result = 0

        while r < len(s):
            # duplicate character can lie in between
            # abba -> at s[2] -> first while has to remove a then b.
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1

            # Add current character
            hashSet.add(s[r])
            # Update result with current window size
            result = max(result, r - l + 1)
            r = r + 1

        return result