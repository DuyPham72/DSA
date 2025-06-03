class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            result = stone1 - stone2
            if result != 0:
                heapq.heappush(stones, result)

        return -stones[0] if len(stones) > 0 else 0