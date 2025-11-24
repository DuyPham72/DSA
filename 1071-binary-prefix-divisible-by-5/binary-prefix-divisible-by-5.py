class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        value = 0
        ans = []
        for num in nums:
            value = (value * 2 + num) % 5
            ans.append(value == 0)

        return ans