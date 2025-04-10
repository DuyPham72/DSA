class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        result = nums[0]

        for num in nums:
            if abs(num) < abs(result):
                result = num

        if abs(result) in nums:
            return abs(result)

        return result                    