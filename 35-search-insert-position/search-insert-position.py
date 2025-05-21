class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1 

        while l < r:
            m = l + ((r-l)//2)  
            if nums[m] < target: 
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
            
        if nums[l] < target:
            return l + 1
        else:
            return l