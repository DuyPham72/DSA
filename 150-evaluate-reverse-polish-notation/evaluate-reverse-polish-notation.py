class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        valid = set('+-*/')
        for c in tokens:
            if c in valid:
                right = stack.pop()
                left = stack.pop()
                if c == '+':
                    stack.append(left + right)
                elif c == '-':
                    stack.append(left - right)
                elif c == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(left / right)) 
            else:
                stack.append(int(c))

        return stack.pop()