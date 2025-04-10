class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []

        if nums == []:
            return result

        start = nums[0]

        for i in range(1, len(nums) + 1):
            if  i < len(nums) and nums[i] == nums[i-1] + 1:
                continue

            if nums[i-1] == start:
                result.append(f"{start}")
            else:
                result.append(f"{start}->{nums[i-1]}")

            if  i < len(nums):
                start = nums[i]

        return result