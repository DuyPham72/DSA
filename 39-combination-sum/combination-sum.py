class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, temp = [], []

        def backtrack(x, cur_sum):
            if sum(temp) > target or x == len(candidates):
                return
            if sum(temp) == target:
                result.append(temp[:])
                return

            backtrack(x+1, cur_sum)

            temp.append(candidates[x])
            backtrack(x, cur_sum + candidates[x])
            temp.pop()

        backtrack(0, 0)
        return result