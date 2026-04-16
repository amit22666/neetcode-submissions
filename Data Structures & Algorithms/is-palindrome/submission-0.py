class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Define a function that takes s (a string) as input

        # Step 2: Initialize an empty list (or string) to store only valid characters
        valid_chars = []

        # Step 3: Loop through each character in s
        for char in s:
            # Step 3.1: Check if the character is alphanumeric (letter or digit)
            if char.isalnum():
                # Step 3.2: If it is, convert it to lowercase and add it to the list
                char = char.lower()
                valid_chars.append(char)

        # Step 4: Join the list of characters into a cleaned string
        clean_string = "".join(valid_chars)
        # Step 5: Initialize two pointers: one at the start (left), one at the end (right)
        left = 0
        right = len(clean_string) - 1

        # Step 6: While left is less than right
        while left < right:
            # Step 6.1: If characters at left and right are not the same, return False
            if clean_string[left] != clean_string[right]:
                return False
            # Step 6.2: Move left pointer one step forward
            left = left + 1
            # Step 6.3: Move right pointer one step backward
            right = right - 1

        # Step 7: If the loop finishes without returning False, return True
        return True


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # Step 1: Store only alphanumeric characters in lowercase
#         valid_chars = []

#         for char in s:
#             if char.isalnum():   # shorter way instead of isalpha() or isdigit()
#                 char = char.lower()
#                 valid_chars.append(char)

#         # Step 2: Join into a cleaned string
#         clean_string = "".join(valid_chars)

#         # Step 3: Two-pointer check
#         left, right = 0, len(clean_string) - 1
#         while left < right:
#             if clean_string[left] != clean_string[right]:
#                 return False
#             left += 1
#             right -= 1

#         return True
