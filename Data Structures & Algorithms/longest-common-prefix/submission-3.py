class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        initial_prefix = strs[0]

        for i in range(1, len(strs)):
            cur_str = strs[i]
            while self.is_prefix(initial_prefix, cur_str) == False:
                initial_prefix = initial_prefix[:-1]
                if initial_prefix == "":
                    return ""
        return initial_prefix

    def is_prefix(self, initial_prefix, cur_str):
        if len(initial_prefix) > len(cur_str):
            return False
        for i in range(len(initial_prefix)):
            if initial_prefix[i] != cur_str[i]:
                return False
        return True
