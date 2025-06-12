class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new_nums = set(nums)
        
        temp = 0
        while temp in new_nums:
            temp += 1

        return temp