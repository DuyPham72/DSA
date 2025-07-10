class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        nums.sort()

        return [i**2 for i in nums]