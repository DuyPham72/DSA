class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num == val:
                continue

            nums[i] = num
            i += 1

        return i