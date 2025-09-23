class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n*(n+1))//2
        temp = 0
        
        for num in nums:
            temp += num
            
        return total-temp