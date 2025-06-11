class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        j = n-1
        extra = 1

        while extra != 0:
            if j == -1:
                digits.insert(0, 1)
                extra = 0
            else:
                temp = digits[j] + 1
                digits[j] = temp % 10
                extra = temp // 10
                j -= 1

        return digits