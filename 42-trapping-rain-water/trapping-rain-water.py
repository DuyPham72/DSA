class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        l, r = 0, n-1
        lvalue = height[l]
        rvalue = height[r]

        result = 0

        while l < r:
            if lvalue < rvalue:
                l += 1
                lvalue = max(lvalue, height[l])
                result += lvalue - height[l]
            else:
                r -= 1
                rvalue = max(rvalue, height[r])
                result += rvalue - height[r]

        return result