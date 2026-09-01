# ways(i) = ways(i+1)            // take 1 digit
#         + ways(i+2) if s[i:i+2] is between "10" and "26"

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def solve(i):
            # i = how many characters are left
            if i == 0:
                return 1

            if i in memo:
                return memo[i]

            index = len(s) - i   # starting index of remaining substring

            # invalid if starting with '0'
            if s[index] == '0':
                return 0

            # take 1 digit
            ways = solve(i - 1)

            # take 2 digits if valid
            if i >= 2:
                two = int(s[index:index+2])
                if 10 <= two <= 26:
                    ways += solve(i - 2)

            memo[i] = ways
            return ways
        
        return solve(len(s))

        