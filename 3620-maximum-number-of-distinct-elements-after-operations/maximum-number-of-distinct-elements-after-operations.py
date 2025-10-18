class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = -k
        count = 0

        for num in nums:
            lower = num-k
            upper = num+k

            new_prev = max(prev + 1, lower)
            if new_prev <= upper:
                count += 1
                prev = new_prev
                    
        return count