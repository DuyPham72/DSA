class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        temp = None

        for i, word in enumerate(words):
            value = sorted(word)
            if i > 0 and value == temp:
                continue
            else:
                ans.append(word)
                temp = value

        return ans