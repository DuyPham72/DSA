class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            
            right = dfs(i, j+1)
            left = dfs(i, j-1)
            down = dfs(i+1, j)
            up = dfs(i-1, j)
            return 1 + right + down + left + up

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    temp = dfs(i, j)
                    result = max(result, temp)

        return result