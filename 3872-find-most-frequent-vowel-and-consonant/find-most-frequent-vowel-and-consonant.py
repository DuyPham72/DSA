class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = set('aeiou')
        freq_dict = Counter(s)
        
        max_vowel = 0
        max_conso = 0

        for key, value in freq_dict.items():
            if key in vowel:
                if value > max_vowel:
                    max_vowel = value 
            else:
                if value > max_conso:
                    max_conso = value 
        
        return max_vowel + max_conso