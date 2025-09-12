class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = True
        for i in range(len(digits)-1, -1, -1):
            if temp == True:
                digits[i] += 1
                temp = False

            if digits[i] == 10:
                digits[i] = 0
                temp = True

        if temp == True:
            digits.insert(0, 1)

        return digits