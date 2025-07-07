class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Step 1: Sort events by start day
        events.sort()
        total_days = max(end for _, end in events)
        
        event_index = 0
        min_heap = []
        attended = 0
        
        # Step 2: Iterate day by day
        for day in range(1, total_days + 1):
            # Step 3: Add events starting today
            while event_index < len(events) and events[event_index][0] == day:
                heapq.heappush(min_heap, events[event_index][1])
                event_index += 1
            
            # Step 4: Remove expired events
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            
            # Step 5: Attend the event that ends earliest
            if min_heap:
                heapq.heappop(min_heap)
                attended += 1
        
        return attended