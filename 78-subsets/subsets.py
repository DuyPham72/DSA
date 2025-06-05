class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, temp = [], []

        def backtracking(i = 0):
            if i == len(nums):
                result.append(temp.copy())
                return

            backtracking(i+1)

            temp.append(nums[i])
            backtracking(i+1)
            temp.pop()

        backtracking()

        return result