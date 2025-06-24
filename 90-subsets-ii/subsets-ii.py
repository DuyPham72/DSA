class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result, temp = [], []
        seen = set()
        def backtrack(x):
            if tuple(temp) not in seen:
                result.append(temp[:])
                seen.add(tuple(temp[:]))

            for i in range(x, len(nums)):
                temp.append(nums[i])
                backtrack(i+1)
                temp.pop()

        backtrack(0)
        return result