class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        count = [0]*value
        for num in nums:
            count[num % value] += 1

        mex = min(count)
        return mex*value + count.index(mex)