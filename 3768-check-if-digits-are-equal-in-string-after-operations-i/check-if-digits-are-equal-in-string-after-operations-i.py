class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        while n > 2:
            temp = ''
            for i in range(1, n):
                temp += str((int(s[i]) + int(s[i-1])) % 10)

            s = temp
            n -= 1

        return True if s[0] == s[1] else False