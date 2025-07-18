class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        result = []
        count = 0
        while count < n and intervals[count][1] < newInterval[0]:
            result.append(intervals[count])
            count += 1

        while count < n and intervals[count][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[count][0])
            newInterval[1] = max(newInterval[1], intervals[count][1])
            count += 1

        result.append(newInterval)

        while count < n:
            result.append(intervals[count])
            count+= 1

        return result