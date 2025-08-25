class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}

        for i, num in enumerate(nums):
            value = target - num
            if value in temp:
                return [temp.get(value), i]
            
            temp[num] = i