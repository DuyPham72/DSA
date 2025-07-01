class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        if len(s) == i:
            return 0

        sign = False
        if s[i] == '-':
            sign = True
            i += 1
        elif s[i] == '+':
            i += 1

        valid = set('0123456789')
        ans = 0
        while i < len(s) and s[i] in valid:
            digit = int(s[i])
            ans = ans * 10 + digit
            i += 1

        ans = -ans if sign else ans
        if ans < -2**31:
            return -2**31
        if ans > 2**31 - 1:
            return 2**31 - 1
        return ans