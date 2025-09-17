class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = [[] for _ in range(numRows)]

        row = 0
        sign = 1
        for c in s:
            if row == 0:
                sign = 1
            elif row == numRows-1:
                sign = -1

            ans[row].append(c)
            row += sign

        temp = ''
        for row in ans:
            temp += ''.join(row)

        return temp