class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            rev = rev * 10 + pop
        
        rev *= sign
        return rev if INT_MIN <= rev <= INT_MAX else 0

#         Sign handling

# Negative numbers should remain negative after reversal.

# Example: -123 → -321.

# Overflow check

# 32‑bit signed integer range:

# Min = -2147483648 (-2^31)
# one bit represent sign => negative or postive
# Max = 2147483647 (2^31 - 1)

# Digit extraction

# Use modulo (% 10) to get the last digit.

# Use integer division (// 10) to chop off the last digit.

# Build reversed number step by step.

    