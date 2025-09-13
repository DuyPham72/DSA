class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = set('aeiou')
        freq_dict = Counter(s)
        
        max_vowel = 0
        max_conso = 0

        for key, value in freq_dict.items():
            if key in vowel:
                max_vowel = value if value > max_vowel else max_vowel
            else:
                max_conso = value if value > max_conso else max_conso
        
        return max_vowel + max_conso