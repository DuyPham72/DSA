class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result, temp = [], []
        n = len(nums)
        used = [False] * n

        def backtrack():
            if len(temp) == n:
                result.append(temp[:])
                return

            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                temp.append(nums[i])
                backtrack()
                temp.pop()
                used[i] = False

        backtrack()
        return result