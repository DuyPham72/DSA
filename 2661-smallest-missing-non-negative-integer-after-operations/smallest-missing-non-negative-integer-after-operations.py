class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = [0] * value
        for x in nums:
            cnt[x % value] += 1

        mn = min(cnt)
        return mn * value + cnt.index(mn)