from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        We have to track two maximums.
        - current_maximum
          - maximum sum for subArray ending at this position
        - global_maximum
          - global maximum for ending at position prior to current position
        """


        current_maximum = nums[0]
        global_maximum = nums[0]
        for n in nums[1:]:
            current_maximum = max(n, n + current_maximum)
            global_maximum = max(global_maximum, current_maximum)
        return global_maximum

