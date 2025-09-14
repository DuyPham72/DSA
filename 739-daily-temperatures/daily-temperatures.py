class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i, temp in enumerate(temperatures[::-1], 1):
            while stack and temp >= stack[-1][1]:
                stack.pop()

            if not stack:
                ans[n-i] = 0
            else:
                key, value = stack[-1]
                ans[n-i] = i - key

            stack.append([i, temp])

        return ans