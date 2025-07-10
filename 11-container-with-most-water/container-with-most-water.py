class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        ans = 0

        while l<r:
            row = r-l
            column = min(height[l], height[r])

            ans = max(ans, row*column)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans