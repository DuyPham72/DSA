class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        longest = 0
        arr = [0] * 26
        l = 0

        for r in range(n):
            arr[ord(s[r]) - 65] += 1
            while (r-l+1) - max(arr) > k:
                arr[ord(s[l]) - 65] -= 1
                l += 1

            longest = max(longest, r-l+1)

        return longest