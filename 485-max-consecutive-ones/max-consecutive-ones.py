class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = curr = 0
        for num in nums:
            if num:
                curr += 1
            else:
                maxx = max(maxx, curr)
                curr = 0

        maxx = max(maxx, curr)
        return maxx