class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, temp = [], []

        def backtracking():
            if len(temp) == len(nums):
                result.append(temp[:])
                return

            for i in range(len(nums)):
                if nums[i] not in temp:
                    temp.append(nums[i])
                    backtracking()
                    temp.pop()

        backtracking()
        return result