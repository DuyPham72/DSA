class Solution:
    def intersect(self, num1: List[int], num2: List[int]) -> List[int]:
        n = len(num1)
        m = len(num2)

        if n > m:
            small, large = num2, num1
        else:
            small, large = num1, num2

        result = []
        small_hash = Counter(small)
        for num in large:
            if small_hash.get(num, 0) > 0:
                result.append(num)
                small_hash[num] -= 1

        return result