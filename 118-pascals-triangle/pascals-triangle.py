class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for depth in range(1, numRows+1):
            temp = [1] * depth
            n = len(temp)
            if n > 2:
                for i in range(1, n-1):
                    temp[i] = result[depth-2][i-1] + result[depth-2][i]
            
            result.append(temp[:])
                
        return result