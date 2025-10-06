class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longest = 0
        curr = 0
        temp = []
        idx = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
                longest = max(longest, curr)
            elif nums[i] == 0 and len(temp) < k:
                temp.append(i)
                curr += 1
                longest = max(longest, curr)
            else:
                temp.append(i)
                curr = i - temp[idx]
                idx += 1

        return longest