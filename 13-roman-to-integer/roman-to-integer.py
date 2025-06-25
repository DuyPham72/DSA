class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        ans = 0
        prev = None
        for letter in s:
            integer = roman[letter]
            if prev != None and prev < integer:
                ans -= 2*prev

            ans += integer
            prev = integer

        return ans