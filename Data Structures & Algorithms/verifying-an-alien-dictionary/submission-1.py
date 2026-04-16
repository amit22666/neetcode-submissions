class Solution:
    def isAlienSorted(self, words, order):
        rank = {c: i for i, c in enumerate(order)}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            found_diff = False  # <--- we track manually
            
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    # compare alien ranks
                    if rank[w1[j]] > rank[w2[j]]:
                        return False
                    found_diff = True
                    break
            
            # If no difference found, check length rule
            if not found_diff:
                if len(w1) > len(w2):
                    return False
        
        return True

# see first submission for -> for else concept

# Why is there an else after a for loop?

# Because in Python:

# 👉 for … else means: the else executes ONLY if the loop finished normally, without hitting a break.

# 🌟 Intuition: “else runs only when break does NOT happen”

# Think of it like:

# If we found a different character → we hit break → else does NOT run.

# If we never found a different character → loop ends normally → else runs.

# So the else is used for the prefix case:
