class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        ans = [0]*(n+1)

        for cite in citations:
            ans[min(cite, n)] += 1

        print(ans)

        h = n
        paper_count = ans[h]
        while h > paper_count:
            h -= 1
            paper_count += ans[h]
        
        return h