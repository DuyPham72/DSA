class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sett = set(nums)
        ans = 0

        for num in sett:
            if num-1 in sett:
                continue

            count = 1
            while num + count in sett:
                count += 1

            ans = max(ans, count)

        return ans