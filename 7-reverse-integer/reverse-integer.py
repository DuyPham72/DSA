class Solution:
    def reverse(self, x: int) -> int:
        temp = list(str(x))
        sign = 0 if temp[0] != '-' else 1

        for i in range((len(temp)-sign)//2):
            temp[i+sign], temp[-1-i] = temp[-1-i], temp[i+sign]

        ans = int(''.join(temp))
        return 0 if ans > 2**31 - 1 or ans < -2**31 else ans