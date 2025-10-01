class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)-1
        l, r = 0, n
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        
        if target >= nums[l] and target <= nums[n]:
            left, right = l, n
        elif target >= nums[0] and target <= nums[l-1]:
            left, right = 0, l-1
        else:
            return -1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                return mid

        return -1