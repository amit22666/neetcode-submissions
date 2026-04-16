class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Define a function that takes two strings s and t as input
        
        # Step 2: If the lengths of s and t are not the same, return False immediately 
        # (because they can’t be anagrams if sizes differ)
        if len(s) != len(t):
            return False
        
        
        # Step 3: Create an empty dictionary (hashmap) to count character frequencies from s
        char_countOfS = {}
        
            

        # Step 4: Loop through each character in s
            # Step 4.1: For each character, increase its count in the dictionary
        for char in s:
            char_countOfS[char] = char_countOfS.get(char,0) +1

        # Step 5: Loop through each character in t
        for char_t in t:
            # Step 5.1: If the character is not in the dictionary , return False
            if char_t not in char_countOfS:
                return False
            # (because t has a character not present in s)
            # Step 5.2: Otherwise, decrease the count of that character in the dictionary
            char_countOfS[char_t] = char_countOfS[char_t] - 1
            # Step 5.3: If the count goes below zero, return False 
            # (because t has more of that character than s)
            if char_countOfS[char_t] < 0:
                return False

        # Step 6: After looping, if all character counts are balanced, return True
        return True

        