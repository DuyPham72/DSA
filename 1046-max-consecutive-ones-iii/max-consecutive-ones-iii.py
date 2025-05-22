class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxx = 0
        zero = 0
        l = 0

        for i in range(n):
            if nums[i] == 0:
                zero += 1

            while zero > k:
                if nums[l] == 0:
                    zero -= 1
                l += 1

            maxx = max(maxx, i-l+1)

        return maxx