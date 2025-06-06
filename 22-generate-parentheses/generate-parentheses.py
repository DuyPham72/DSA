class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, temp = [], []

        def backtrack(openn, close):
            if close == n:
                result.append(''.join(temp))
                return

            if openn < n:
                temp.append("(")
                backtrack(openn + 1, close)
                temp.pop()

            if openn > close:
                temp.append(")")
                backtrack(openn, close + 1)
                temp.pop()

        backtrack(0,0)
        return result

        