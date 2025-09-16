class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena = len(a)
        lenb = len(b)
        bigger = a if lena > lenb else b

        temp = 0
        ans = ''

        i = 0
        while i < min(lena, lenb):
            value = int(a[-1-i]) +  int(b[-1-i]) + temp

            if value % 2 == 0:
                ans += '0'
            else:
                ans += '1'

            temp = 0 if value < 2 else 1
            i += 1
            
        while i < max(lena, lenb):
            value = temp + int(bigger[-1-i])
            
            if value % 2 == 0:
                ans += '0'
            elif value == 1:
                ans += '1'

            temp = 0 if value < 2 else 1
            i += 1

        if temp == 1:
            ans += '1'

        return ans[::-1]