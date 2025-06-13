class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = curr = 0
        for num in nums:
            if num:
                curr += 1
                maxx = max(maxx, curr)
            else:
                curr = 0

        return maxx