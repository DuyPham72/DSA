class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}

        for i, value in enumerate(numbers):
            other = target - value
            if other in d:
                return [d[other]+1, i+1]
            
            d[value] = i