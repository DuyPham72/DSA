class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if r*c != m*n:
            return mat

        row = col = 0
        ans = [[0 for _ in range(c)] for _ in range(r)]

        for i in range(r):
            for j in range(c):
                ans[i][j] = mat[row][col]
                col += 1
                if col == n:
                    col = 0
                    row += 1

        return ans