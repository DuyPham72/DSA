class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, temp = [], []

        def backtrack(i):
            if sum(temp) == target:
                result.append(temp[:])
                return
            elif sum(temp) > target or i == len(candidates):
                return

            for x in range(i, len(candidates)):
                temp.append(candidates[x])
                backtrack(x)
                temp.pop()

        backtrack(0)

        return result