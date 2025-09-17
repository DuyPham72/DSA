class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                idx, value = stack.pop()
                largest = max(largest, value*(i-idx))
                start = idx

            stack.append([start, height])

        for i, height in stack:
            largest = max(largest, height * (len(heights)-i))

        return largest