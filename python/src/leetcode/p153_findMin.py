from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [3,4,5,1,2]
        """
        start = 0
        end = len(nums) - 1

        def half_index(start, end):
            if start < end:
                return (start + end) // 2
            else:
                idx = (start + end + len(nums)) // 2
                if idx >= len(nums):
                    idx -= len(nums)
                return idx

        while start != end:
            # minimum should be somewhere between start and end
            if nums[start] == nums[end]:
                return nums[start]
            next_half = half_index(start, end)
            # reach to the end
            if next_half == start or next_half == end:
                return min(nums[start], nums[end])

            if nums[start] > nums[next_half]:
                end = next_half
            elif nums[next_half] > nums[end]:
                start = next_half
            else:
                return nums[start]
        return nums[start]
