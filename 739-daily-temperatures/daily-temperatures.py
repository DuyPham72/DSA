class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        length = 1
        
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                temp = stack.pop()
                tem, idx = temp[0], temp[1]
                answer[idx] = i - idx  

            stack.append([temperatures[i], i])

        return answer