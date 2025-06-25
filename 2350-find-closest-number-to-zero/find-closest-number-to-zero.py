class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]

        for num in nums[1:]:
            if abs(num) <= abs(ans):
                ans = num

        return ans if abs(ans) not in nums else abs(ans)