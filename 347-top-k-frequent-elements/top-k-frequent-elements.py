class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        arr = list(counter.items())
        arr.sort(key=lambda x: x[1], reverse=True)

        return [num for num, count in arr[:k]]