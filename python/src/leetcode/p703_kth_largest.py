from typing import List
import heapq

class KthLargest:
    """
    Every time we add new element, we have to compare the new value with current smallest number.
    So, data structure for tracking smallest number in array is useful here
    """

    def __init__(self, k: int, nums: List[int]):
        """
        Heapify the list and makes the length of heap to K
        """
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:

        if self.k > len(self.nums):
            # there is still room for new element,  so just push it anyway
            heapq.heappush(self.nums, val)
        else:
            kth_largest = self.nums[0] if len(self.nums) > 0 else None

            if  (val is None) or val > kth_largest:
                heapq.heappop(self.nums)
                heapq.heappush(self.nums, val)

        return self.nums[0]
