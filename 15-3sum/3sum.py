class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            
            l = i+1
            r = n-1
            while l < r:
                value = nums[i] + nums[l] + nums[r]
                if value > 0:
                    r -= 1
                elif value < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < n and nums[l] == nums[l-1]:
                        l += 1

                    r -= 1
                    while r >= 0 and nums[r] == nums[r+1]:
                        r -= 1

        return ans