class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = set(nums)
        ans = 1

        for num in count:
            if num-1 not in count:
                length = 0

                while (num+length) in count:
                    length += 1

                ans = max(ans, length)

        return ans