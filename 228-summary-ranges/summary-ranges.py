class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        ans = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if nums[i-1] != start:
                    ans.append("{}->{}".format(start, nums[i-1]))
                else:
                    ans.append("{}".format(start))

                start = nums[i]

        if start != nums[-1]:
            ans.append("{}->{}".format(start, nums[-1]))
        else:
            ans.append("{}".format(start))

        return ans