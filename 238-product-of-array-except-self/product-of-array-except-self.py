class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]*n
        right = [1]*n

        for i in range(n-1):
            left[i+1] = left[i] * nums[i]
            right[-i-2] = right[-i-1] * nums[-i-1]

        ans = []
        for i in range(n):
            ans.append(left[i]*right[i])

        return ans