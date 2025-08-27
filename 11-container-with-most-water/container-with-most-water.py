class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1

        ans = 0

        while l < r:
            l_value = height[l]
            r_value = height[r]

            row = r-l
            col = min(l_value, r_value)
            ans = max(ans, row * col)

            if l_value < r_value:
                l += 1
            else:
                r -= 1

        return ans