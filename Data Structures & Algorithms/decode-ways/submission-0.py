# ways(i) = ways(i+1)            // take 1 digit
#         + ways(i+2) if s[i:i+2] is between "10" and "26"

class Solution:
    def numDecodings(self, s: str) -> int:
        
        def solve(n):
            # n = how many characters are left
            if n == 0:
                return 1

            index = len(s) - n   # starting index of remaining substring

            # invalid if starting with '0'
            if s[index] == '0':
                return 0

            # take 1 digit
            ways = solve(n - 1)

            # take 2 digits if valid
            if n >= 2:
                two = int(s[index:index+2])
                if 10 <= two <= 26:
                    ways += solve(n - 2)

            return ways
        
        return solve(len(s))


        