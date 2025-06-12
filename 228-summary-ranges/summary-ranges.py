class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if len(nums) == 0:
            return result

        start = end = nums[0]
        for num in nums[1:]:
            if end != num-1:
                if start != end:
                    result.append(f"{start}->{end}")
                else:
                    result.append(f"{end}")

                start = num
            end = num

        if start != end:
            result.append(f"{start}->{end}")
        else:
            result.append(f"{end}")

        return result