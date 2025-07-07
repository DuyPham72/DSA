class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        dvd = abs(dividend)
        dvs = abs(divisor)
        quotient = 0

        while dvs <= dvd:
            i = 0
            while (dvs << i) <= dvd:
                i += 1
            
            i -= 1
            dvd -= (dvs << i)
            quotient += (1 << i)

        if (dividend < 0) != (divisor < 0):
            return -quotient
        return quotient