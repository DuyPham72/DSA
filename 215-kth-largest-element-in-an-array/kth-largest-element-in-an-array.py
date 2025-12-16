import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums = [-num for num in nums]
        heapq.heapify(nums)

        temp = None
        for i in range(k):
            temp = heapq.heappop(nums)

        return -temp