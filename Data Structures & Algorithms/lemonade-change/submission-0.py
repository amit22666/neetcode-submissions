class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for b in bills:
            if b == 5:
                five = five + 1
            elif b == 10:
                ten = ten + 1
                five = five - 1
            elif ten > 0:
                ten = ten - 1
                five = five - 1
            else:
                five = five - 3
            if five < 0:
                return False
        return True


        