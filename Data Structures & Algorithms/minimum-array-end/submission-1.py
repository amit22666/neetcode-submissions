# not understood copilot appoach

# but 2nd appoach
# n ka n+1 ke saath or karenege toh result milega
# wo result wo smallest number milega. jiska n ke saath and krne pr n milta hai
# yeh kaam x times repeat krna hai

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        ans = x
        bit = 0
        for i in range(64):  # up to 64 bits
            if (x >> i) & 1 == 0:  # if bit not set in x
                if (n >> bit) & 1:
                    ans |= 1 << i
                bit += 1
        return ans
