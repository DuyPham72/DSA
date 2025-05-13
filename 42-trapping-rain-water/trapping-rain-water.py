class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left, right = 0, 0
        left_array = [0]*n
        right_array = [0]*n

        for i in range(n):
            j  = -i -1

            left_array[i] = left
            right_array[j] = right
            left = max(left, height[i])
            right = max(right, height[j])

        result = 0
        for i in range(n):
            expect = min(left_array[i], right_array[i])

            if expect - height[i] > 0:
                result += expect - height[i]

        return result
