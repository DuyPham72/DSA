class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_set = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        vowel = []

        for c in s:
            if c in vowel_set:
                vowel.append([ord(c), c])

        vowel = sorted(vowel, key=lambda x: x[0])
        s = list(s)

        j = 0
        for i in range(len(s)):
            if s[i] in vowel_set:
                idx, value = vowel[j]
                s[i] = value
                j += 1

        return "".join(s)