class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = sorted(points, key=lambda x: x[0]**2 + x[1]**2)
        return ans[:k]