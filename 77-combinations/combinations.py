class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, temp = [], []

        def backtracking(x):
            if len(temp) == k:
                result.append(temp[:])
                return

            for i in range(x, n+1):
                if i not in temp:
                    temp.append(i)
                    backtracking(i)
                    temp.pop()

        backtracking(1)
        return result