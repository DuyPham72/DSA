import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        preprocess = re.sub(r'[^a-z0-9]', '', s.lower())
        
        l = 0
        r = len(preprocess)-1
        while l<r:
            if preprocess[l] != preprocess[r]:
                return False

            l +=1 
            r -= 1

        return True