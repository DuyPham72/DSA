class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        temp = None
        for i in range(len(nums)):
            if nums[i] == 1:
                if temp is not None and i - temp <= k:
                    return False
                temp = i

        return True