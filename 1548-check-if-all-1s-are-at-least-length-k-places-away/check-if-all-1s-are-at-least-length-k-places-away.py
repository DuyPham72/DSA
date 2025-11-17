class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        value = [i for i, num in enumerate(nums) if num == 1]

        for i in range(1, len(value)):
            if value[i] - value[i-1] - 1 < k:
                return False

        return True