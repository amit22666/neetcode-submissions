class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        def expand(left: int, right: int) -> str:
            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                left -= 1
                right += 1

            return s[left + 1:right]

        for i in range(len(s)):
            # Odd-length palindrome, such as "aba"
            odd = expand(i, i)

            # Even-length palindrome, such as "abba"
            even = expand(i, i + 1)

            if len(odd) > len(longest):
                longest = odd

            if len(even) > len(longest):
                longest = even

        return longest