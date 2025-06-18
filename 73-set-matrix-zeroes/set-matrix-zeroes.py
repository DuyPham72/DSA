class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        zero_row = set()
        zero_col = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)

        for r in zero_row:
            matrix[r] = len(matrix[r]) * [0]

        for c in zero_col:
            for row in matrix:
                row[c] = 0