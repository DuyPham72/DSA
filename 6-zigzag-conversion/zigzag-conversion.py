class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        d = 1
        i = 0

        matrix = [[] for _ in range(numRows)]

        for word in s:
            matrix[i].append(word)

            if i == 0:
                d = 1
            elif i == numRows-1:
                d = -1
            
            i += d

        result = ""
        for i in range(numRows):
            result += ''.join(matrix[i])

        return result