class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result, temp = [], []

        def backtracking():
            if len(temp) == n:
                result.append(temp[:])
                return
            
            for i in range(n):
                if nums[i] not in temp:
                    temp.append(nums[i])
                    backtracking()
                    temp.pop()

        backtracking()
        return result