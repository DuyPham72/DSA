class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []

        for i in range(len(points)):
            x, y = points[i]
            arr.append([points[i],x**2 + y**2])

        arr.sort(key=lambda x: x[1])

        result = []
        for i in arr[:k]:
            result.append(i[0])

        return result