from typing import List
import heapq

class Solution:
    """
    Given an integer array nums and an integer k, return the k most frequent elements.
    You may return the answer in any order.

    Example 1:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]

    Example 2:
        Input: nums = [1], k = 1
        Output: [1]
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Strategy:
            1. countup the list from the top and buid mapping of number and count
            2. use heap to get k most frequent one
        """

        # count up
        count_map = {}

        for n in nums:
            if n in count_map.keys():
                count_map[n] += 1
            else:
                count_map[n] = 1

        # convert them to tuple to use in heap
        # NOTE: negate the count, since heapq is min-heap
        count_list = [(-v, k) for k, v in count_map.items()]

        heapq.heapify(count_list)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(count_list)[1])
        return result




