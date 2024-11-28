from typing import List

class Solution:
    """
    Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

    A subarray is a contiguous non-empty sequence of elements within an array.


    Example 1:

    Input: nums = [1,1,1], k = 2
    Output: 2
    Example 2:

    Input: nums = [1,2,3], k = 3
    Output: 2

    """
    def subarraySum(self,  nums: List[int],  k: int) -> int:

        prefix_sum_count = {0: 1}
        current_sum = 0
        result = 0

        for n in nums:
            current_sum += n


            if current_sum - k in prefix_sum_count:
                result += prefix_sum_count[current_sum - k]

            if current_sum in prefix_sum_count:
                prefix_sum_count[current_sum] += 1
            else:
                prefix_sum_count[current_sum] = 1

        return result
