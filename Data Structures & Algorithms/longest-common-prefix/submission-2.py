class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Step 1: Define a function that accepts strs (a list of strings)


        # Step 2: If strs is empty, immediately return "" (no common prefix)
        if len(strs) == 0:
            return ""

        # Step 3: Assume the first string in strs is the initial prefix
        initial_prefix = strs[0]

        # Step 4: Loop through the rest of the strings in strs
        for i in range (1,len(strs)):

        # Step 4.1: While the current string does not start with the prefix
        #           keep reducing the prefix by removing its last character
            cur_str = strs[i]
            while self.is_prefix(initial_prefix, cur_str) == False:
                initial_prefix = initial_prefix[:-1]
                if initial_prefix == "":
                    return ""

        # Step 4.2: If the prefix becomes empty, return "" (no common prefix)
        
        # Step 5: After checking all strings, return the remaining prefix
        return initial_prefix
        # Step 6: Test with given examples to confirm the output
    def is_prefix(self, initial_prefix, cur_str):
        if len(initial_prefix) > len(cur_str):
            return False
        for i in range(len(initial_prefix)):
            if initial_prefix[i] != cur_str[i]:
                return False
        return True