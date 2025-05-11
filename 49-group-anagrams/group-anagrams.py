class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            key = [0 for _ in range(26)]

            for letter in word:
                key[ord(letter) - ord('a')] += 1

            key = tuple(key)
            result[key].append(word)

        return [value for value in result.values()]
