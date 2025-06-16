class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        eat = len(candyType) // 2
        distinct_candy = len(set(candyType))

        return min(eat, distinct_candy)