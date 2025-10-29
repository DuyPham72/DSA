class Solution:
    def smallestNumber(self, n: int) -> int:
        value = len(str(bin(n))[2:])
        
        ans = ['1'] * value

        return int(''.join(ans), 2)