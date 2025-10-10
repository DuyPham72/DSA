class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        value = nums[0]
        for num in nums[1:]:
            if num == value:
                count += 1
            else:
                count -= 1
                if count == 0:
                    value = num
                    count = 1

        return value