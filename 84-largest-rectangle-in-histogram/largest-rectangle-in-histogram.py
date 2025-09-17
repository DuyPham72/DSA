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

        n = len(heights)
        for i, h in stack:
            largest = max(largest, h * (n-i))

        return largest