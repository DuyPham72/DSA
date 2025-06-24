class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash2 = {}
        for i, word in enumerate(list2):
            hash2[word] = i

        same_word = defaultdict(list)
        for i, word in enumerate(list1):
            if word in hash2:
                same_word[i+hash2[word]].append(word)

        minn = min(same_word.keys())
        return same_word[minn]