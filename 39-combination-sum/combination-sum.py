class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        temp = []
        n = len(candidates)

        def backtrack(temp, start):
            value = sum(temp)
            if value > target:
                return
            if sum(temp) == target:
                ans.append(temp[:])
                return

            for i in range(start, n):
                temp.append(candidates[i])
                backtrack(temp, i)
                temp.pop()

        backtrack(temp, 0)
        return ans