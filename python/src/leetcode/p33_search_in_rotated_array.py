
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        [5, 1, 3]
        """
        left = 0
        right = len(nums) - 1


        while left < right:
            mid = (left + right) // 2

            if nums[left] <= target <= nums[mid]:
                right = mid 
            elif nums[left] > nums[mid] and not nums[mid] < target < nums[left]:
                right = mid 
            else:
                left = mid + 1

        if nums[left] == target or nums[right] == target:
            return left
        else:
            return -1

