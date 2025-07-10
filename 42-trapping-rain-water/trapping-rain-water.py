class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        l_value = height[l]
        r_value = height[r]

        ans = 0
        while l<r:
            if l_value < r_value:
                l += 1
                if l_value > height[l]:
                    ans += l_value - height[l]
                else:
                    l_value = height[l]
            else:
                r -= 1
                if r_value > height[r]:
                    ans += r_value - height[r]
                else:
                    r_value = height[r]

        return ans