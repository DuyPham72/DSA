class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")

        result = []
        for word in words:
            count1 = count2 = count3 = 0
            for letter in word:
                if letter.lower() in first:
                    count1 += 1
                elif letter.lower() in second:
                    count2 += 1
                else:
                    count3 += 1

            if (count1 or count2 or count3) == len(word):
                result.append(word)

        return result                