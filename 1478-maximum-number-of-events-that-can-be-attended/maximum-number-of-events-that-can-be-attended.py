class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        ans = 0
        heap = []
        max_end = max(end for _, end in events)

        i = 0
        for day in range(1, max_end+1):
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1

            while heap and heap[0] < day:
                heapq.heappop(heap)
            
            if heap:
                heapq.heappop(heap)
                ans += 1

        return ans