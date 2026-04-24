class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Repeat till -> carry is 0
        # sum = a ^ b
        # carry = (a&b) << 1 (right shift by 1)
        MASK = 0xFFFFFFF
        MAX_INT = 0x7FFFFFF
        while b != 0:
            carry = (a&b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        # handle negative numbers
        return a if a <= MAX_INT else ~(a^MASK)

# We need the ~(a ^ MASK) part specifically to convert the final 32‑bit result into a proper negative integer in Python. 
# That’s where ~(a ^ MASK) comes in:

# a ^ MASK → flips the extra high bits beyond 32.

# ~(...) → applies bitwise NOT, which gives the correct negative value.

# MASK → keeps numbers inside 32-bit range.
# MAX_INT → helps interpret whether the final result is positive or negative.

# why we need bask and max_int
# Great question — the reason we need MASK (0xFFFFFFFF) and MAX_INT (0x7FFFFFFF) in the Python solution is because Python integers are unbounded, while in most languages (like C, C++, Java) integers are fixed-width (32-bit). To simulate the same behavior, we explicitly restrict values to 32 bits.

# 🔍 Why MASK?
# MASK = 0xFFFFFFFF (all 32 bits set to 1).

# After each XOR and carry operation, we apply & MASK to force the result back into 32-bit range.

# Without this, Python would happily keep growing the integer size, and the bitwise simulation would break for negative numbers.

# 👉 Think of MASK as a boundary fence that keeps numbers inside the 32-bit playground.

# 🔍 Why MAX_INT?
# MAX_INT = 0x7FFFFFFF (the largest positive 32-bit signed integer = 2,147,483,647).

# After finishing the loop, if the result a is within positive range, we return it directly.

# If a exceeds MAX_INT, it means the number should be interpreted as negative in 32-bit signed arithmetic.

# To convert it back, we use:

# python
# ~(a ^ MASK)
# which flips the bits and gives the correct negative value.

# 👉 Think of MAX_INT as the cutoff point between positive and negative numbers in signed 32-bit representation.

# ⚡ Quick Example
# Suppose we add -1 + 2:

# In 32-bit signed arithmetic, result = 1.

# Python without masking would keep growing bits and misinterpret -1.

# With MASK and MAX_INT, we correctly simulate the wrap-around and sign handling.



