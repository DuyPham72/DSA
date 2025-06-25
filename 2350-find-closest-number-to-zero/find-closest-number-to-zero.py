class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = float('inf')

        for num in nums:
            if abs(num) <= abs(ans):
                ans = num

        return ans if abs(ans) not in nums else abs(ans)