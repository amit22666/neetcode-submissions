# My input - In dp we explore all states. but here we are greedy for
#opening bracket. Based on count of opening bracket valid or not
# regex can take any value

class Solution:
    def checkValidString(self, s: str) -> bool:
        # for what and how we are geedy in this problem\

        MaxOpenBracket = 0
        MinOpenBracket = 0

        for c in s:

            if c == '(':
                MaxOpenBracket = MaxOpenBracket + 1
                MinOpenBracket = MinOpenBracket + 1
            elif c == ")":
                MaxOpenBracket = MaxOpenBracket - 1
                MinOpenBracket = MinOpenBracket - 1
            else:
                MaxOpenBracket = MaxOpenBracket + 1 # if regex is openbracket
                MinOpenBracket = MinOpenBracket - 1 # if regex is closebracket
            if MinOpenBracket < 0:
                MinOpenBracket = 0  # Trap
            if MaxOpenBracket < 0:
                return False
        return MinOpenBracket == 0 # Trap