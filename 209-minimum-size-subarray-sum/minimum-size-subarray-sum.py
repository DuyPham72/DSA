class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        ans = float('inf')
        temp = 0
        l = 0

        for r, value in enumerate(nums):
            temp += value

            while temp >= target:
                ans = min(ans, r-l+1)
                temp -= nums[l]
                l += 1

        return 0 if ans == float('inf') else ans