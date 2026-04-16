# QUESTION EXPLAINED
# How Do We Compare Two Words in Alien Order?

# To check if the list is sorted, we only need to compare each word with the next word, just like checking a dictionary.

# Example:

# ["hello", "leetcode"]


# Compare:

# 'h' vs 'l'

# If 'h' comes before 'l' in alien order → good.

# If first letters are same → compare 2nd letters.
# If second are same → compare 3rd letters.
# And so on…

# If all letters are same except length:

# ["app", "apple"]


# This is sorted because:

# “app” is shorter → should come first.

# BUT this is UNSORTED:

# ["apple", "app"]


# Because longer word appears before shorter prefix → wrong order.



class Solution:
    def isAlienSorted(self, words, order):
        # Step 1: create a rank map for each alien letter
        rank = {ch: i for i, ch in enumerate(order)}
        
        # Step 2: compare each word with the next
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            
            # Step 3: compare characters of w1 and w2
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    # compare using alien ranks
                    if rank[w1[j]] > rank[w2[j]]:
                        return False  # wrong order
                    break
            else:
                # All characters matched so far (prefix case)
                # Now shorter word must come first
                if len(w1) > len(w2):
                    return False
        
        return True


        
