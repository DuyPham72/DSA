class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        result = 0
        heap = [(0,0)]
        seen = set()

        while heap:
            distance, i = heapq.heappop(heap)
            if i in seen:
                continue

            seen.add(i)
            result += distance
            xi, yi = points[i]
            
            for j in range(len(points)):
                if j not in seen:
                    xj, yj = points[j]
                    dis = abs(xi-xj) + abs(yi - yj)
                    heapq.heappush(heap, (dis, j))

        return result