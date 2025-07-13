class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        temp = 0
        for num in nums[1:]:
            if num == nums[i]:
                continue
            
            i += 1
            nums[i] = num

        return i+1