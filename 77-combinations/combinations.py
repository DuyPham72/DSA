class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, temp = [], []

        def backtrack(i):
            if len(temp) == k:
                result.append(temp[:])
                return

            for x in range(i, n+1):
                temp.append(x)
                backtrack(x+1)
                temp.pop()
                        
        backtrack(1)

        return result