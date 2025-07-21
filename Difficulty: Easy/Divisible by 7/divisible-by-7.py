class Solution:
    def isdivisible7(self, num):
        remainder = 0
        for digit in num:
            remainder = (remainder * 10 + int(digit)) % 7
        return int(remainder == 0)
