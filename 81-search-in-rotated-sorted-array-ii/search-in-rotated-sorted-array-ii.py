class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True

            # When we can’t tell which side is sorted, skip one end
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1

            # Left half is sorted
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # Otherwise, right half must be sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False