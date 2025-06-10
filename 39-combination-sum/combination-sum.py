class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, temp = [], []

        def backtrack(x, cur_sum):
            if cur_sum > target:
                return
            if cur_sum == target:
                result.append(temp[:])
                return

            for i in range(x, len(candidates)):
                temp.append(candidates[i])
                backtrack(i, cur_sum + candidates[i])
                temp.pop()

        backtrack(0, 0)
        return result