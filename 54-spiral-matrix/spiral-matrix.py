class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, bot = 0, m
        left, right = 0, n

        res = []
        while top < bot and left < right:
            for j in range(top, right):
                res.append(matrix[top][j])
            top += 1

            for i in range(top, bot):
                res.append(matrix[i][right-1])
            right -= 1

            if top < bot:
                for j in range(right-1, left-1, -1):
                    res.append(matrix[bot-1][j])
                bot -= 1

            if left < right:
                for i in range(bot-1, top-1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res