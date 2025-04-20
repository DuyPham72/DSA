class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paper = [0]*(n+1)

        for c in citations:
            paper[min(n, c)] += 1

        h = n
        paper_count = paper[h]

        while h > paper_count:
            h -= 1
            paper_count += paper[h]

        return h