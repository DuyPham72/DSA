class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        
        a_queue = deque()
        a_seen = set()

        p_queue = deque()
        p_seen = set()

        for i in range(n):
            p_queue.append((0, i))
            p_seen.add((0, i))

        for j in range(1, m):
            p_queue.append((j, 0))
            p_seen.add((j, 0))

        for i in range(m):
            a_queue.append((i, n-1))
            a_seen.add((i, n-1))

        for j in range(n-1):
            a_queue.append((m-1, j))
            a_seen.add((m-1, j))

        def coord(queue, seen):
            while queue:
                i, j = queue.popleft()
                for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r, c = i + x, j + y
                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j] and (r, c) not in seen:
                        seen.add((r, c))
                        queue.append((r, c))

        coord(p_queue, p_seen)
        coord(a_queue, a_seen)
        return list(p_seen.intersection(a_seen))