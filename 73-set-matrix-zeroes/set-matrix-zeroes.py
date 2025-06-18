class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        zeros_location = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros_location.append([i, j])

        for pair in zeros_location:
            row, col = pair

            for i in range(m):
                if matrix[i][col] != 0:
                    matrix[i][col] = 0

            for j in range(n):
                if matrix[row][j] != 0:
                    matrix[row][j] = 0