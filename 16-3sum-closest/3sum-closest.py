class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        min_diff = abs(closest_sum - target)

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = n-1
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                diff = total - target
                if diff == 0:
                    return total

                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    closest_sum = total

                if total < target:
                    l += 1
                else:
                    r -= 1
                
        return closest_sum