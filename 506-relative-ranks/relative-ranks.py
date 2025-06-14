class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        answer = [0] * n

        hashmap ={}
        for i in range(n):
            hashmap[score[i]] = i

        sort_score = sorted(score)
        sort_answer = [0] * n

        for i in range(n-1, -1, -1):
            rank = n - i
            if rank == 1:
                sort_answer[i] = "Gold Medal"
            elif rank == 2:
                sort_answer[i] = "Silver Medal"
            elif rank == 3:
                sort_answer[i] = "Bronze Medal"
            else:
                sort_answer[i] = str(rank)

        for i in range(n):
            idx = hashmap.get(sort_score[i])
            answer[idx] = sort_answer[i]

        return answer