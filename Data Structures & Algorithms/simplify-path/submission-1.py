class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        stack = []

        for part in parts:
            if part == "..":
                if stack:
                    stack.pop()
            elif part != "." and part != "": # what is the reason for and
                stack.append(part)

        return "/" + "/".join(stack)