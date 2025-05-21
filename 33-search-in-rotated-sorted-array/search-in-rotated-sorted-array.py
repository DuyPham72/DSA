class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1

        while l<r:
            m = l + ((r-l) // 2)
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m

        pivot = l
        if pivot == 0:
            l = 0
            r = n-1
        elif nums[0] <= target and nums[pivot-1] >= target:
            l = 0
            r = pivot-1      
        else:
            l = pivot
            r = n-1

        while l <= r:
            m = l + ((r-l) // 2)
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                return m

        return -1