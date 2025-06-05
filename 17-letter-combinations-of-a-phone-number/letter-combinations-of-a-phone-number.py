class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dic = { 2: 'abc',
                3: 'def',
                4: 'ghi',
                5: 'jkl',
                6: 'mno',
                7: 'pqrs',
                8: 'tuv',
                9: 'wxyz'}

        n = len(digits)
        result, temp = [], []

        def backtrack(i):
            if len(temp) == n:
                result.append(''.join(temp))
                return

            for x in range(i, n):
                num = int(digits[x])
                letters = dic[num]

                for word in letters:
                    temp.extend(word)
                    backtrack(x+1)
                    temp.pop()

        backtrack(0)
        return result