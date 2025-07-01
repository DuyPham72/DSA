class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        hold = [""] * numRows
        idx = 0
        direction = 1
        
        for w in s:
            if idx == 0:
                direction = 1
            elif idx == numRows-1:
                direction = -1
            
            hold[idx] += w
            idx += direction

        return "".join(hold)