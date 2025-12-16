class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = [(-freq, key) for key, freq in count.items()]
        heapq.heapify(heap)

        ans = []
        for _ in range(k):
            freq, key = heapq.heappop(heap)
            ans.append(key)
        
        return ans