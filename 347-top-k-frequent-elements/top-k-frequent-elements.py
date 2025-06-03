class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        arr = []

        for num, freq in counter.items():
            if len(arr) < k:
                heapq.heappush(arr, (freq, num))
            else:
                heapq.heappushpop(arr, (freq, num))

        return [num for freq, num in arr]