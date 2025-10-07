class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        ans = 0
        while l < r:
            row = r-l
            col = min(height[l], height[r])
            ans = max(ans, row*col)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans