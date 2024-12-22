from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        Basic idea is loop through and keep Kth-smallest set
        We use max-heap and push the new element if it is smaller than current max

        We try to reduce the computational cost by early returning if the element is largher than current max
        """

        k_smallest = []


        for i in nums1:
            for j in nums2:
                if len(k_smallest) < k:
                    heapq.heappush(k_smallest, (- (i + j), (i, j)))
                else:
                    if k_smallest[0][0]  * -1 > i + j:
                        heapq.heappop(k_smallest)
                        heapq.heappush(k_smallest, ( - (i + j), (i,  j)))
                    else:
                        # we can early return since the array is sorted
                        break
        return [pairs for _, pairs in k_smallest]


