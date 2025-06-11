class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[counter] = nums[read]
                counter += 1
        
        return counter