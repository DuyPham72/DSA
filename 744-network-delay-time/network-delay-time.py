class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, time in times:
            graph[start].append((end, time))

        min_time = {}
        min_heap = [(0, k)]

        while min_heap:
            time, i = heapq.heappop(min_heap)
            if i in min_time:
                continue

            min_time[i] = time
            for end, t in graph[i]:
                if end not in min_time:
                    heapq.heappush(min_heap, (t + time, end))

        return max(min_time.values()) if len(min_time) == n else -1