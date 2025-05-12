class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        set_nums = set(nums)
        result = 1

        for num in set_nums:
            if (num - 1) not in set_nums:
                length = 0

                while (num + length) in set_nums:
                    length += 1
                    result = max(result, length)

        return result