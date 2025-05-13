class Solution:
    def isValid(self, s: str) -> bool:
        temp = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                temp.append(c)
            else:
                if temp:
                    if c == ')' and temp[-1] == '(':
                        temp.pop()
                    elif c == ']' and temp[-1] == '[':
                        temp.pop()
                    elif c == '}' and temp[-1] == '{':
                        temp.pop()
                    else:
                        return False
                else:
                    return False    
        
        if not temp:
            return True
        else:
            return False