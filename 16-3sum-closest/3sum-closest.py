class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('inf')
        total = 0

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = n-1
            while l < r:
                value = nums[i] + nums[l] + nums[r]
                result = abs(value - target)

                if result < closest:
                    closest = result
                    total = value

                if value < target:
                    l += 1
                else:
                    r -= 1

        return total