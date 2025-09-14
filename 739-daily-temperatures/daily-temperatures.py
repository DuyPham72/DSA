class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            temp = temperatures[i]

            # pop all smaller or equal temps
            while stack and temp >= stack[-1][1]:
                stack.pop()

            # if stack not empty, next warmer day is at stack[-1][0]
            if stack:
                ans[i] = stack[-1][0] - i
            else:
                ans[i] = 0

            # push current day onto stack
            stack.append((i, temp))

        return ans