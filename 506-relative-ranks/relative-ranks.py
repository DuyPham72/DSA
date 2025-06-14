class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        answer = [''] * n

        sort_idx = sorted(range(n), key= lambda i: score[i], reverse=True)

        for rank, i in enumerate(sort_idx, start=1):
            if rank == 1:
                answer[i] = "Gold Medal"
            elif rank == 2:
                answer[i] = "Silver Medal"
            elif rank == 3:
                answer[i] = "Bronze Medal"
            else:
                answer[i] = str(rank)


        return answer