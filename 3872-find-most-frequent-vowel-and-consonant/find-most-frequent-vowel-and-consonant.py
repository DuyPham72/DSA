class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = set('aeiou')

        vowel_set = []
        consonant_set = []
        for c in s:
            if c in vowel:
                vowel_set.append(c)
            else:
                consonant_set.append(c)

        vowel_dict = Counter(vowel_set)
        consonant_dict = Counter(consonant_set)
        
        max_vowel = 0
        max_conso = 0
        for i in vowel_dict.values():
            if i > max_vowel:
                max_vowel = i
        for i in consonant_dict.values():
            if i > max_conso:
                max_conso = i

        return max_vowel + max_conso