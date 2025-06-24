class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        word = defaultdict(list)

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    word[i+j].append(list1[i])

        minn = min(word.keys())
        return word[minn]