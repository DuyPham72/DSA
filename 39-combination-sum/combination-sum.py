class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)

        def backtrack(temp=[], start=0):
            total = sum(temp)
            if total > target:
                return
            if total == target:
                ans.append(temp[:])
                return

            for i in range(start, n):
                temp.append(candidates[i])
                backtrack(temp, i)
                temp.pop()

        backtrack()
        return ans