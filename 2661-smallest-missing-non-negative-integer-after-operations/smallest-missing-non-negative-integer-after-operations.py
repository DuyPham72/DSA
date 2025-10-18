class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        bins = Counter(num % value for num in nums)

        ans = 0
        while bins[ans % value] > 0:
            bins[ans % value] -= 1
            ans += 1

        return ans