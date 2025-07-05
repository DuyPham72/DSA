class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)

        ans = -1
        for key, value in counter.items():
            if key == value:
                ans = key if key > ans else ans

        return ans