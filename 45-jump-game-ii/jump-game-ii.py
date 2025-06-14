class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = end = farthest = 0

        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                jumps += 1
                end = farthest

        return jumps