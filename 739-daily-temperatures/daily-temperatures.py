class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [[temperatures[0],0]]
        length = 1
        
        for i in range(1, len(temperatures)):
            temp = stack.pop()
            tem, idx = temp[0], temp[1]

            if temperatures[i] > tem:
                while tem < temperatures[i]:
                    answer[idx] = i - idx  

                    if stack:
                        temp = stack.pop()
                        tem, idx = temp[0], temp[1]
                    else:
                        break  

            if tem >= temperatures[i]:
                stack.append([tem, idx])

            stack.append([temperatures[i], i])

        return answer