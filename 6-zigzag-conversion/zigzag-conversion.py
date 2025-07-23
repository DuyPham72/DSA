class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        hold = [''] * numRows
        index = 0
        direction = 1

        for w in s:
            if index == 0:
                direction = 1
            elif index == numRows-1:
                direction = -1

            hold[index] += w
            index += direction

        return ''.join(hold)