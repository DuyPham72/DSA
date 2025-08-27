class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        n1 = len(num1)
        n2 = len(num2)
        ans = [0]*(n1+n2)

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                total = mul + ans[i+j+1]
                ans[i+j+1] = total % 10
                ans[i+j] += total // 10 
                
        product = ''.join(map(str,ans)).lstrip('0')
        return product