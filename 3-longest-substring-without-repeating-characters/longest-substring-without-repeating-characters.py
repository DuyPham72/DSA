class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()
        longest = idx = 0

        for i in range(len(s)):
            while s[i] in temp:
                temp.remove(s[idx])
                idx += 1

            temp.add(s[i])
            longest = max(longest, i-idx+1)

        return longest