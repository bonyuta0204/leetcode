from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return 0

        left = 0
        right = len(nums) - 1

        if nums[right] < target:
            return right + 1

        if nums[right] == target:
            return right 

        if nums[0] > target:
            return 0

        while True:
            mid = (left + right) // 2

            if left == right -1 and nums[left] != target:
                return right


            if nums[mid] < target:
                left = mid

            elif nums[mid] > target:
                right = mid
            else:
                return mid



