class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = -k
        count = 0

        for num in nums:
            lower = num-k
            upper = num+k

            if prev < lower:
                prev = lower
            else:
                prev += 1
            
            if upper >= prev:
                count += 1
            else:
                prev -= 1
                    
        return count