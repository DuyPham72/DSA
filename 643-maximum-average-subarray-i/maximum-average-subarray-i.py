class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        ans = summ
        for i in range(k, len(nums)):
            summ += nums[i]
            summ -= nums[i-k]
            if summ > ans:
                ans = summ

        return ans/k