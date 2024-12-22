from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """

        example

        1, 3, 5, 7, 9, 10
        2, 4, 6, 8, 9, 10

        """

        result = []

        heap = []

        for i in range(len(nums1)):
            heap.append((nums1[i] + nums2[0], i, 0))

        heapq.heapify(heap)


        while len(result) < k:
            print(heap)
            _, i, j = heapq.heappop(heap)

            result.append((nums1[i], nums2[j]))

            if j < len(nums2) - 1:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1],  i, j + 1))

        return result


