class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        ans = []

        while l<=r:
            left = nums[l]**2
            right = nums[r]**2

            if left > right:
                ans.append(left) 
                l += 1
            else: 
                ans.append(right)
                r -= 1

        ans.reverse()
        return ans 