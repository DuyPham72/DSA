class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        delete = True
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if delete:
                    i, j = l + 1, r
                    ok1 = True
                    while i < j:
                        if s[i] != s[j]:
                            ok1 = False
                            break
                        i += 1
                        j -= 1

                    i, j = l, r - 1
                    ok2 = True
                    while i < j:
                        if s[i] != s[j]:
                            ok2 = False
                            break
                        i += 1
                        j -= 1

                    return ok1 or ok2
                else:
                    return False

        return True