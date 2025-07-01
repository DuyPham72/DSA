class Solution:
    def reverse(self, x: int) -> int:
        num = int(str(abs(x))[::-1])
        if num > 2**31 - 1:
            return 0
        return -num if x < 0 else num