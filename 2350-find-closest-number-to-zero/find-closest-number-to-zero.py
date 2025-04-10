class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        result = nums[0]

        for num in nums:
            if abs(num) < abs(result):
                result = num
            elif abs(num) == abs(result):
                if num > result:
                    result = num

        return result                    