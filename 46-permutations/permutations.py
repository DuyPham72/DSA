class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, temp = [], []

        def backtracking():
            if len(temp) == len(nums):
                result.append(temp.copy())
                return

            for x in nums:
                if x not in temp:
                    temp.append(x)
                    backtracking()
                    temp.pop()

        backtracking()

        return result