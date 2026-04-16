class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) <= 1:
            return s
        
        start = 0
        max_len = 1
        
        # Function to expand around the center
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # When loop breaks, indices l and r are 1 step beyond the palindrome
            return r - l - 1, l + 1  # length, start_index
        
        for i in range(len(s)):
            # Odd length palindrome (center at i)
            len1, st1 = expand(i, i)
            if len1 > max_len:
                max_len = len1
                start = st1
            
            # Even length palindrome (center between i and i+1)
            len2, st2 = expand(i, i + 1)
            if len2 > max_len:
                max_len = len2
                start = st2
        
        return s[start:start + max_len]
