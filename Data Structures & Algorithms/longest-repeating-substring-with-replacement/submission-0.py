class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # thoda increase in difficulty
        # window mein one distinct character
        # property break ho toh window shrink karo

        # but k false characters allowed hai
        # usse jada nhi
        # means window size (r-l+1) - k -> distint hone chahiye
        
        # aaababa -> max frequency  
        
        # length - maxf <= k

        freq = {}
        res = 0
        l = 0
        maxFreq = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0) + 1
            # trick to calculate max freq
            maxFreq = max(maxFreq, freq[s[r]])  # update incrementally
            window_size = r - l + 1
            repacement = window_size - maxFreq
            while repacement > k:
                freq[s[l]] -= 1
                l = l + 1
                window_size = r-l+1
                repacement = window_size - maxFreq
            res = max(res, r-l+1)
            
        return res



# maxFreq = 0
# for r in range(len(s)):
#     freq[s[r]] = freq.get(s[r], 0) + 1
#     maxFreq = max(maxFreq, freq[s[r]])
#     while (r - l + 1) - maxFreq > k:
#         freq[s[l]] -= 1
#         l += 1
#     res = max(res, r - l + 1)

        
            


        