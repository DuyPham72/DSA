class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = {}

        for num in nums:
            if num not in result:
                result[num] = 1
            else:
                result[num] += 1

        for key, value in result.items():
            if value >= 2:
                return True

        return False 