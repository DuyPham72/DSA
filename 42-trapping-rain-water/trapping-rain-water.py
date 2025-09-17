class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        l_value = height[l]
        r_value = height[r]

        ans = 0
        while l < r:
            if l_value < r_value:
                l += 1
                l_value = max(l_value, height[l])
                ans += l_value - height[l]
            else:
                r -= 1
                r_value = max(r_value, height[r])
                ans += r_value - height[r]

        return ans