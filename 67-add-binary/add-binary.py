class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_value = 0
        b_value = 0
        
        for i, value in enumerate(a[::-1]):
            a_value += int(value) * (2**i)

        for i, value in enumerate(b[::-1]):
            b_value += int(value) * (2**i)

        temp = a_value + b_value

        if temp == 0:
            return "0"

        ans = ''
        while temp != 0:
            ans += str(temp%2)
            temp = temp//2

        return ans[::-1]