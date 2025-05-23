class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        l = 0
        ans = 0

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            temp = r-l+1
            ans = max(ans, temp)
            sett.add(s[r])

        return ans