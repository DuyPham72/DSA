class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1

        if n == i:
            return 0

        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        ans = 0
        while i < n and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            i += 1

        ans *= sign
        return max(-2**31, min(ans, 2**31 - 1))