class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        maxx = []
        for num in nums:
            if num:
                curr += 1
            else:
                maxx.append(curr)
                curr = 0

        maxx.append(curr)
        return max(maxx)