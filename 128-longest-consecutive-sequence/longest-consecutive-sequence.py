class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        temp = set(nums)
        result = 0

        for num in temp:
            if (num-1) not in temp:
                length = 1

                while (num + length) in temp:
                    length += 1
                    
                result = max(result, length)

        return result