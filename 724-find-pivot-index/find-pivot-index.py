class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum1 = 0
        sum2 = sum(nums[1:])

        for i in range(len(nums)):
            if sum1 == sum2:
                return i
            
            sum1 += nums[i]
            if i < len(nums)-1:
                sum2 -= nums[i+1]

        return -1