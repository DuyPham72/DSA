class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []

        for i, h in enumerate(heights):
            temp = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                largest = max(largest, height * (i-idx))
                temp = idx
            stack.append([temp, h])

        for i, h in stack:
            largest = max(largest, h * (len(heights)-i))

        return largest