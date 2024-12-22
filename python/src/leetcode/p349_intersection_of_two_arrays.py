from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_set = set(nums1)
        nums2_set = set(nums2)

        result = []

        for n in nums2_set:
            if n in num1_set:
                result.append(n)

        return result
