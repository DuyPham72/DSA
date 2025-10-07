class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        temp = [0]*26
        longest = 0
        i = 0

        for j in range(len(s)):
            temp[ord(s[j])-65] += 1
            while (j-i+1) - max(temp) > k:
                temp[ord(s[i])-65] -= 1
                i += 1

            longest = max(longest, (j-i+1))

        return longest