class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        ans = 0
        for i in range(n):
            t = timeSeries[i]
            end = t + duration

            if i+1 < n:
                ans += min(end, timeSeries[i+1]) - t
            else:
                ans += duration

        return ans