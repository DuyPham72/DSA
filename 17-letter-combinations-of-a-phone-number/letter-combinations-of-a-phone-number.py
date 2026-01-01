class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dicts = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        ans = []
        n = len(digits)
        def backtrack(temp=[], start=0):
            if len(temp) == n:
                ans.append(''.join(temp))
                return

            for i in range(start, n):
                letters = dicts.get(digits[i])
                for letter in letters:
                    temp.append(letter)
                    backtrack(temp, i+1)
                    temp.pop()
        
        backtrack()
        return ans