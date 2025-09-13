class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = True
        i = len(digits)-1

        while temp and i >= 0:
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                temp = False
            i -= 1

        if temp == True:
            digits.insert(0, 1)

        return digits