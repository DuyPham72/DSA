class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result, temp = [], []
        def backtrack(x):
            result.append(temp[:])
                
            prev = None
            for i in range(x, len(nums)):
                if nums[i] != prev:
                    temp.append(nums[i])
                    backtrack(i+1)
                    temp.pop()
                    prev = nums[i]

        backtrack(0)
        return result