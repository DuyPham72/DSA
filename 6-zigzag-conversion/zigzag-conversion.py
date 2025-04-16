class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = [[] for _ in range(numRows)]

        i = 0
        d = 1

        for word in s:
            result[i].append(word)

            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1

            i += d

        answer = []
        for j in range(numRows):
            answer += result[j]

        return "".join(answer)