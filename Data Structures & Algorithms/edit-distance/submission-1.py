class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # dp[i][j] = min operations to convert word1[:i] to word2[:j]
        # lena padta hai taaki hum empty string ke base case ko bhi cover kar saken 
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # # base cases: converting empty string to prefix
        # Pehla loop (for i in range(m+1)) ka matlab hai: agar word2 empty ho aur word1 mein i characters hain, toh usko empty banane ke liye i deletions karne padenge. Matlab delete all characters of word1 to match empty string.
        for i in range(m + 1):
            dp[i][0] = i   # delete all characters
        # Dusra loop (for j in range(n+1)) ka matlab hai: agar word1 empty ho aur word2 mein j characters hain, toh usko banane ke liye j insertions karne padenge. Matlab insert all characters of word2 into empty word1.
        for j in range(n + 1):
            dp[0][j] = j   # insert all characters
        
        # fill dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # jitne operations i-1, j-1 ko banane mein lagenge
                # utne operation i, j ko banane mein lagenge  
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # no operation
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],    # delete ->  word1[:i] ko word2[:j] mein convert karna hai aur tumne last character of word1 delete kar diya, toh problem reduce ho jaati hai word1[:i-1] ko word2[:j] mein convert karne tak.
                        dp[i][j - 1],    # insert
                        dp[i - 1][j - 1] # replace
                    )
        
        return dp[m][n]
# Tricky but later simple
# INSERT
# dp[i][j-1] ka matlab hai: tum word1[:i] ko word2[:j] mein convert karna chahte ho, aur tumne decide kiya ki word2 ka j‑th character insert karoge. Jab tum insert karte ho, toh ab word1[:i] ko word2[:j-1] ke saath match karna bacha hai, kyunki j‑th character toh tumne abhi insert kar diya.

# So interpretation yeh hai:
# j-1 isliye use hota hai kyunki tumne word2 ka j‑th character already handle kar liya by insertion.
# Ab problem reduce ho gayi hai word1[:i] ko word2[:j-1] mein convert karne tak.
# Uske baad ek extra operation (insert) add karna padta hai, jo DP recurrence mein +1 ke through aa jaata hai.
# Ek line mein: dp[i][j-1] represent karta hai ki agar tumne word2 ka j‑th character insert kar diya, toh baaki kaam hai word1[:i] ko word2[:j-1] ke saath match karna.

# REPLACE
# dp[i-1][j-1] ko interpret karne ka matlab hai: agar tum word1[:i] ko word2[:j] mein convert karna chahte ho aur dono strings ke last characters ko ek saath consider karte ho, toh problem reduce ho jaati hai word1[:i-1] ko word2[:j-1] mein convert karne tak.
# Agar word1[i-1] == word2[j-1], toh koi operation nahi lagta, aur directly dp[i][j] = dp[i-1][j-1].
# Agar characters different hain, toh iska matlab hai tum ek replace operation karoge: word1[i-1] ko word2[j-1] se replace karo, aur phir baaki prefix (word1[:i-1] aur word2[:j-1]) ko match karna hoga.
# Ek line mein: dp[i-1][j-1] represent karta hai ki agar tumne dono strings ke last characters ko ek saath handle kar liya (ya toh match ho gaye, ya replace kar diya), toh baaki kaam reduce ho jaata hai unke prefixes ko convert karne tak.
