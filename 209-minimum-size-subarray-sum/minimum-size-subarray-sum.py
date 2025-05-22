class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        shortest = float('inf')
        answer = 0
        l = 0

        for r in range(len(nums)):
            answer += nums[r]

            while answer >= target:
                shortest = min(shortest, r-l+1)
                answer -= nums[l]
                l += 1

        return shortest if shortest != float('inf') else 0