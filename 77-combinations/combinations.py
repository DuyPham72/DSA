class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(temp, start):
            if len(temp) == k:
                ans.append(temp[:])
                return

            for i in range(start, n+1):
                temp.append(i)
                backtrack(temp, i+1)
                temp.pop()

        backtrack([], 1)
        return ans