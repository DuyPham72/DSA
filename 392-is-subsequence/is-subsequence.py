class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        counter = 0
        for i in range(len(t)):
            if t[i] == s[counter]:
                counter += 1

            if counter == len(s):
                return True

        return False