class Solution:
    def isValid(self, word: str) -> bool:
        vowel = 'aeiouAEIOU'
        conso = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
        valid = vowel + conso + '0123456789'

        vowel = set(vowel)
        conso = set(conso)
        valid = set(valid)

        if len(word) < 3:
            return False

        count1 = 0
        count2 = 0
        for c in word:
            if c in vowel:
                count1 +=1
            if c in conso:
                count2 += 1

            if c not in valid:
                return False

        return True if count1 > 0 and count2 > 0 else False