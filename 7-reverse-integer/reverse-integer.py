class Solution:
    def reverse(self, x: int) -> int:
        if len(str(x)) == 1:
            return x

        num = str(abs(x))
        num = num[::-1]

        i = 0
        while num[i] == '0':
            i += 1

        ans = int(num[i:])
        if ans < pow(-2, 31) or ans > pow(2, 31)-1:
            return 0

        return - int(num[i:]) if x < 0 else int(num[i:])