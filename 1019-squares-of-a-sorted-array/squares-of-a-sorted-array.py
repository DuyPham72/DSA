class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        ans = []

        while l<=r:
            left = nums[l]**2
            right = nums[r]**2

            if left > right:
                ans.insert(0, left) 
                l += 1
            else: 
                ans.insert(0, right)
                r -= 1

        return ans 