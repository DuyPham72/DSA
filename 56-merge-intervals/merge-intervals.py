class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        result = []
        n = len(intervals)

        temp = intervals[0]

        for i in range(1, n):
            if intervals[i][0] <= temp[1]:
                temp[1] = max(temp[1], intervals[i][1])
            else:
                result.append(temp)
                temp = intervals[i]

        result.append(temp)

        return result