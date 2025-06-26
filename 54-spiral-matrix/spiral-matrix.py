class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, bot = 0, m
        left, right = 0, n

        result = []
        while top < bot and left < right:
            for j in range(top, right):
                result.append(matrix[top][j])
            top += 1

            for i in range(top, bot):
                result.append(matrix[i][right-1])
            right -= 1

            if top < bot:
                for j in range(right-1, left-1, -1):
                    result.append(matrix[bot-1][j])
                bot -= 1

            if left < right:
                for i in range(bot-1, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
            
        return result