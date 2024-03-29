from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # binary search
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return r
