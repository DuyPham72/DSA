class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, temp = [], []
        n = len(nums)

        def backtrack(temp):
            if len(temp) == n:
                ans.append(temp[:])
                return

            for i in range(n):
                if nums[i] not in temp:
                    temp.append(nums[i])
                    backtrack(temp)
                    temp.pop()

        backtrack(temp)
        return ans