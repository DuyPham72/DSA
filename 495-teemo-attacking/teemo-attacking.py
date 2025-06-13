class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        res = duration
        for i in range(1, n):
            gap = timeSeries[i] - timeSeries[i - 1]
            if gap >= duration:
                res += duration
            else:
                res += gap
        return res