from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [3,4,5,1,2]
        """
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        return min(nums[start], nums[end])

