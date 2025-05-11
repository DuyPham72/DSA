class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        table = Counter(nums)

        for key, value in table.items():
            if value > (n // 2):
                return key