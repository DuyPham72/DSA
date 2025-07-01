class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        num = abs(x)

        while num != 0:
            digit = num % 10
            ans = ans * 10 + digit
            num //= 10

        ans = -ans if x < 0 else ans

        if ans > 2**31 - 1 or ans < -2**31:
            return 0

        return ans