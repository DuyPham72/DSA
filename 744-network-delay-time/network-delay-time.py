class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s, e, d in times:
            graph[s].append((e, d))

        min_time = {}
        min_heap = [(0, k)] # distance, from source to that point
        while min_heap:
            distance, i = heapq.heappop(min_heap)

            if i not in min_time:
                min_time[i] = distance

                for end, dis in graph[i]:
                    if end not in min_time:
                        heapq.heappush(min_heap, (distance + dis, end))

        return max(min_time.values()) if len(min_time) == n else -1