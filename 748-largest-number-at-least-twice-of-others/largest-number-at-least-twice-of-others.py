class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = [None, -1]
        second_largest = [None, -1]

        for i, num in enumerate(nums):
            if num > largest[1]:
                second_largest = largest
                largest = [i, num]
            elif num > second_largest[1]:
                second_largest = [i, num]

        return largest[0] if largest[1] // 2 >= second_largest[1] else -1