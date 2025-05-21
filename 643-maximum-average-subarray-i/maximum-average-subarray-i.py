class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        ans = 0

        for i in range(k):
            ans += nums[i]

        avg = ans/k
        for i in range(k, n):
            ans += nums[i]
            ans -= nums[i-k]
            avg = max(avg, ans/k)

        return avg