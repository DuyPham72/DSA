class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        temp = l = 0

        for r, value in enumerate(nums):
            temp += nums[r]

            while temp >= target:
                ans = min(ans, r-l+1)
                temp -= nums[l]
                l += 1

        return 0 if ans == float('inf') else ans