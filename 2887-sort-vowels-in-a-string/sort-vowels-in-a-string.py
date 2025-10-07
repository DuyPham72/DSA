class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        vowels_set = sorted(c for c in s if c in vowels)

        s = list(s)
        idx = 0
        for i, c in enumerate(s):
            if c in vowels:
                s[i] = vowels_set[idx]
                idx += 1

        return ''.join(s)