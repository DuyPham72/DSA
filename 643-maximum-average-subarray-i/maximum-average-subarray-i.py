class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        ans = total
        for i in range(k, len(nums)):
            total += nums[i] - nums[i-k]
            if total > ans:
                ans = total

        return ans/k