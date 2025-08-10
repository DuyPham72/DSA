class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0
        temp = None
        for roman in s:
            integer = dic[roman]
            if temp != None and integer > temp:
                res -= 2*temp

            res += integer
            temp = integer

        return res