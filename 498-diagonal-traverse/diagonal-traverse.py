class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = []

        for x in range(m + n - 1):
            # valid rows i for which j = x - i is inside [0..n-1]
            start_row = max(0, x - (n - 1))
            end_row   = min(m - 1, x)

            if x % 2 == 0:
                # even diagonal: traverse upwards (i decreases)
                for i in range(end_row, start_row - 1, -1):
                    ans.append(mat[i][x - i])
            else:
                # odd diagonal: traverse downwards (i increases)
                for i in range(start_row, end_row + 1):
                    ans.append(mat[i][x - i])

        return ans