class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        result = 0
        count = Counter(answers)

        for answer, freq in count.items():
            group_size = answer + 1
            num_groups = (freq + answer) // group_size
            result += num_groups * group_size

        return result