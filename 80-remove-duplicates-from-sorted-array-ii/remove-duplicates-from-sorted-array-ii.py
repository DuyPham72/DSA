class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        i = 0
        temp = nums[0]
        for num in nums:
            if temp != num:
                count = 0
                temp = num

            if num == temp and count < 2:
                nums[i] = num
                i += 1
                count += 1

        return i