class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = 0
        n = len(digits)
        for i in range(n-1, -1, -1):
            value = digits[i] + 1

            if value == 10:
                digits[i] = value%10
                temp = 1
            else:
                digits[i] = value
                temp = 0
                break

        if temp == 1:
            digits.insert(0, temp)

        return digits