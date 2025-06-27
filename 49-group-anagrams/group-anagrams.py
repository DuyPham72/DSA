class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for w in strs:
            key = tuple(sorted(w))
            ans[key].append(w)

        return [value for value in ans.values()]