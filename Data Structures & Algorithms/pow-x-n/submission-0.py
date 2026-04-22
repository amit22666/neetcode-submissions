class Solution:
    # Yeh approach fast exponentiation ke naam se jaana jaata hai, aur interview mein expected solution hai.

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        def fastPow(x, n):
            if n == 0:
                return 1
            half = fastPow(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        return fastPow(x, n)


        # myPow(2.0, 5) = 32.0

# Hinglish Trace Summary
# n=5 → odd → half power calculate karo → fastPow(2,2)

# n=2 → even → half power calculate karo → fastPow(2,1)

# n=1 → odd → half power calculate karo → fastPow(2,0) → base case = 1

# Backtrack: fastPow(2,1) = 2, fastPow(2,2) = 4, fastPow(2,5) = 32
