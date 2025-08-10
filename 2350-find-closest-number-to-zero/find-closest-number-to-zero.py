class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        temp = nums[0]

        for num in nums[1:]:
            if abs(num) < abs(temp):
                temp = num
            elif abs(num) == abs(temp):
                temp = num if temp < num else temp

        return temp