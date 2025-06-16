class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        eat = n//2
        distinct_candy = len(set(candyType))

        return min(eat, distinct_candy)