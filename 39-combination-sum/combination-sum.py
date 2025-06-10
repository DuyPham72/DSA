class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, temp = [], []

        def backtrack(x):
            if sum(temp) > target:
                return
            elif sum(temp) == target:
                result.append(temp[:])
                return

            for i in range(x, len(candidates)):
                temp.append(candidates[i])
                backtrack(i)
                temp.pop()

        backtrack(0)
        return result