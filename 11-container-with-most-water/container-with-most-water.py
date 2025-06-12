class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        result = 0

        left = 0
        right = n-1
        while left < right:
            x = right - left
            y = min(height[left], height[right])
            result = max(result, x*y)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result