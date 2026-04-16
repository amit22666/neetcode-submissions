class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        
        def expand(l, r):
            nonlocal count
            # Expand while it's a palindrome
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1       # every match = one palindromic substring
                l -= 1
                r += 1
        
        for i in range(n):
            # Odd-length palindromes (center at i)
            expand(i, i)
            
            # Even-length palindromes (center between i and i+1)
            expand(i, i + 1)
        
        return count
