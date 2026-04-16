class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Step 1: Define a function that takes strs (list of strings) as input

        # Step 2: Create an empty dictionary (hashmap) to group anagrams
        group_anagram = {}
        # Key: a representation of the word's characters (like sorted string)
        # Value: list of words that belong to this anagram group

        # Step 3: Loop through each word in strs
        for word in strs:
            # Step 3.1: Sort the characters of the word (so all anagrams share the same sorted key)
            sorted_word = tuple(sorted(word))
            # Step 3.2: Use the sorted word (as a string or tuple) as the key in the dictionary
            if sorted_word not in group_anagram:
            # Step 3.3: If the key is not in the dictionary, initialize it with an empty list
                group_anagram[sorted_word] = []
            # Step 3.4: Append the current word to the list for that key
            # group_anagram = append(group_anagram[sorted_word], word)
            group_anagram[sorted_word].append(word)

        answer = []
        # Step 4: After processing all words, take all the lists (values) from the dictionary
        for key, words_list in group_anagram.items():
            answer.append(words_list)


        # Step 5: Return these lists as the final grouped anagrams
        return answer


# def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # Step 1: Dictionary to group anagrams
#         group_anagram = {}

#         # Step 2: Loop through each word in strs
#         for word in strs:
#             # Sort characters and use tuple as key
#             sorted_word = tuple(sorted(word))
#             if sorted_word not in group_anagram:
#                 group_anagram[sorted_word] = []
#             group_anagram[sorted_word].append(word)

#         # Step 3: Return grouped anagrams
#         return list(group_anagram.values())
        