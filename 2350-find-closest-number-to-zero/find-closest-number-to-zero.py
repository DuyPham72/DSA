class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]

        for num in nums[1:]:
            if abs(num) < abs(ans):
                ans = num
            elif abs(num) == abs(ans):
                if ans < num:
                    ans = num

        return ans