class Solution:
    def isValid(self, s: str) -> bool:
        # Step 1: Define a function that takes s (a string) as input

        # Step 2: Create a stack (empty list) to keep track of open brackets
        open_brackets = []

        # Step 3: Create a dictionary (hashmap) that maps each closing bracket to its matching opening bracket
        # Example: {')': '(', ']': '[', '}': '{'}
        matching_bracket = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        # Step 4: Loop through each character in s
        for char in s:
            # Step 4.1: If the character is an opening bracket ('(', '[', '{')
                # Push it (append) onto the stack
                if char == '(' or char == '[' or char == '{':
                    open_brackets.append(char)
            # Step 4.2: Else (it must be a closing bracket)
                else:
                    # Step 4.2.1: If the stack is empty, return False (no opening bracket to match)
                    if len(open_brackets) == 0:
                        return False
                    # Step 4.2.2: Pop the top element from the stack
                    last_open_bracket = open_brackets.pop()
                    # Step 4.2.3: Check if the popped element matches the expected opening bracket from the dictionary
                        # If not, return False
                    if last_open_bracket != matching_bracket[char]:
                        return False

        # Step 5: After the loop, if the stack is empty return True (all brackets matched correctly)
        if len(open_brackets) == 0:
            return True
        # Otherwise, return False (some opening brackets were not closed)
        return False

        