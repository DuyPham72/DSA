class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        ans = total/k
        for i in range(k, len(nums)):
            total += nums[i]
            total -= nums[i-k]
            ans = max(ans, total / k)

        return ans