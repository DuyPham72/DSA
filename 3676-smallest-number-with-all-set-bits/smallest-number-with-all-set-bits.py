class Solution:
    def smallestNumber(self, n: int) -> int:
        value = list(str(bin(n))[2:])
        
        temp = Counter(value)
        if len(temp.keys()) == 1:
            return n

        for i, num in enumerate(value):
            if num == '0':
                value[i] = '1'

        return int(''.join(value), 2)