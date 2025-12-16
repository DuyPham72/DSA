class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        
        return list(ans.keys())[:k]