class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        # Helper function: ek number ke digits ka square sum nikalna
        def getSquareSum(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        # Loop jab tak 1 nahi milta ya cycle detect nahi hota
        while n != 1:
            if n in visited:   # agar cycle detect ho gaya
                return False
            visited.add(n)     # current number ko mark karo
            n = getSquareSum(n)  # next number calculate karo

        return True  # agar 1 mil gaya toh happy number hai
