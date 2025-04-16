class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 1
        counter = 0

        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                counter = 0
                j += 1
            elif counter == 0 and nums[i] == nums[i-1]:
                nums[j] = nums[i]
                counter= 1
                j += 1 

        return j