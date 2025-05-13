class Solution:
    def isValid(self, s: str) -> bool:
        temp = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                temp.append(s[i])
            else:
                if temp:
                    if s[i] == ')' and temp[-1] == '(':
                        temp.pop()
                    elif s[i] == ']' and temp[-1] == '[':
                        temp.pop()
                    elif s[i] == '}' and temp[-1] == '{':
                        temp.pop()
                    else:
                        return False
                else:
                    return False 
        
        if not temp:
            return True
        else:
            return False