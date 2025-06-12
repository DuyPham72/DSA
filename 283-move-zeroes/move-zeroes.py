class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[temp] = nums[i]
                temp += 1

        for i in range(temp, len(nums)):
            nums[i] = 0