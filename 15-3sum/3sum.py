class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sort_nums = sorted(nums)
        result = []

        for i in range(n):
            if i > 0 and sort_nums[i] == sort_nums[i-1]:
                continue
            elif sort_nums[i] > 0:
                break
            
            left = i+1
            right = n-1
            while left < right:
                total = sort_nums[i] + sort_nums[left] + sort_nums[right]
                if total > 0: 
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    result.append([sort_nums[i], sort_nums[left], sort_nums[right]])
                    left += 1
                    right -= 1

                    while left < n and sort_nums[left] == sort_nums[left-1]:
                        left += 1
                    while right > 0 and sort_nums[right] == sort_nums[right+1]:
                        right -= 1

        return result