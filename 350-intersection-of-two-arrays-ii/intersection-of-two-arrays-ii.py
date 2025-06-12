class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        small, large = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        small_hash = Counter(small)

        result = []
        for num in large:
            if small_hash.get(num, 0) > 0:
                result.append(num)
                small_hash[num] -= 1

        return result