class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        ans = []
        end = temp = 0
        for i in range(n):
            t = timeSeries[i]

            end = t + duration - 1
            temp = end - t + 1

            if i+1 < n and timeSeries[i+1] <= end:
                ans.append(timeSeries[i+1] - t)
            else:
                ans.append(temp)

        return sum(ans)