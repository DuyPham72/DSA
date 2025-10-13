class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        temp = None

        for i in range(len(words)):
            value = sorted(words[i])
            if i > 0 and value == temp:
                continue
            else:
                ans.append(words[i])
                temp = value

        return ans