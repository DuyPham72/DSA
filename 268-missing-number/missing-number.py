class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        temp = set(nums)
        n = len(nums)

        while n in temp:
            n = n-1

        return n