class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        l = 0
        r = row*col - 1

        while l <= r:
            m = l + ((r-l) // 2)
            i = m // col
            j = m % col

            if matrix[i][j] < target:
                l = m+1
            elif matrix[i][j] > target:
                r = m-1
            else:
                return True

        return False    