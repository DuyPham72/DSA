class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        g = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    g.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        minute = 0
        while g and fresh > 0:
            for _ in range(len(g)):
                i, j = g.popleft()
                for x, y in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                    r, c = i+x, j+y
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        grid[r][c] = 2
                        g.append((r, c))
                        fresh -= 1

            minute += 1

        return minute if fresh == 0 else -1