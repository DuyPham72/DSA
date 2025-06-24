class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        unique = set()
        for i in range(n):
            unique.add(nums[i])

        return True if target in unique else False