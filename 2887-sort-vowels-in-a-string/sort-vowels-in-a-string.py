class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_set = set('aeiouAEIOU')
        vowel = sorted(c for c in s if c in vowel_set)
        print(vowel)

        s = list(s)
        j = 0
        for i in range(len(s)):
            if s[i] in vowel_set:
                s[i] = vowel[j]
                j += 1

        return "".join(s)