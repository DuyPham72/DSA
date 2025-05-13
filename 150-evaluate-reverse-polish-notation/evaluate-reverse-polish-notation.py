import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+' or c == '-' or c == '*' or c == '/':
                operand2 = stack.pop()
                operand1 = stack.pop()
                if c == '+': 
                    stack.append(operand1 + operand2)
                elif c == '-':
                    stack.append(operand1 - operand2)
                elif c == '*':
                    stack.append(operand1 * operand2)
                else:
                    stack.append(int(operand1 / operand2))
            else:
                stack.append(int(c))

        return stack[0]