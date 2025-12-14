import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            new_weight = a - b

            heapq.heappush(stones, new_weight)

        return -heapq.heappop(stones)