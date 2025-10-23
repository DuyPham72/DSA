class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(s)
        s = [int(i) for i in s]
        n = len(s)

        while n > 2:
            for i in range(1, n):
                s[i-1] = (s[i] + s[i-1]) % 10
            n -= 1

        return s[0] == s[1]