class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[:k])
        curr = ans
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            if curr > ans:
                ans = curr

        return ans/k 