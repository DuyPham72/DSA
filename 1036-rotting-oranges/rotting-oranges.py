class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] ==  2:
                    queue.append((i, j))

        minute = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r, c = i+x, j+y
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r, c))
                        fresh -= 1

            minute += 1

        return minute if fresh == 0 else -1