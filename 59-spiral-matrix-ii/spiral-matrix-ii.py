class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, bottom = 0, n-1
        left, right = 0, n-1
        num = 1

        ans = [[0]*n for _ in range(n)]
        while num <= n**2:
            for j in range(left, right + 1):
                ans[top][j] = num
                num += 1
            top += 1

            for i in range(top, bottom + 1):
                ans[i][right] = num
                num += 1
            right -= 1

            for j in range(right, left - 1, -1):
                ans[bottom][j] = num
                num += 1
            bottom -= 1

            for i in range(bottom, top-1, -1):
                ans[i][left] = num
                num += 1
            left += 1

        return ans