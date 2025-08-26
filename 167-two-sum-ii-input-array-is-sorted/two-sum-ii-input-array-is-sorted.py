class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l < r:
            value = numbers[l] + numbers[r]
            if value == target:
                return [l+1, r+1]

            if value > target:
                r -= 1
            else:
                l += 1