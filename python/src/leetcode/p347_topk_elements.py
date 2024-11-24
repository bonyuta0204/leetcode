from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        - count all occurences
        - store the count in key-value structure
        - then we select K smallest value
            - intuitive way is to sort and pack first K element
            - using heap seems more efficient
        """

        freq_dict = {}

        # count up numbers
        for n in nums:
            if n in freq_dict:
                freq_dict[n] += 1
            else:
                freq_dict[n] = 1

        freq_list = []
        # turn the dict into list of tuples for heap operation
        for n, count in freq_dict.items():
            freq_list.append((count, n))

        # heapify and select K top freq
        # Note: python heap is min-heap
        freq_list_negated = [(-c, n) for (c, n) in freq_list]

        heapq.heapify(freq_list_negated)

        result = []

        # pick k element
        for i in range(k):
            m = heapq.heappop()
            result.append(m[1])
