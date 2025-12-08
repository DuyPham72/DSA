class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}

        for i in range(len(nums)):
            other = target - nums[i]
            if temp.get(other, -1) != -1:
                return [temp[other], i]

            temp[nums[i]] = i