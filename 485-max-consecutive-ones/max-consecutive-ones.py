class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        curr = 0

        for num in nums:
            if num == 1:
                curr += 1
                maxx = max(maxx, curr)
            else:
                curr = 0

        return maxx