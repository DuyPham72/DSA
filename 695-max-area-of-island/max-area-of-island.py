class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            return 1 + dfs(i, j+1) + dfs(i, j-1) + dfs(i+1, j) + dfs(i-1, j)

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result = max(result, dfs(i, j))

        return result