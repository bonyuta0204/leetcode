from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for n in nums:
            idx = bisect.bisect_left(tails, n)
            if idx < len(tails):
                tails[idx] = n
            else:
                tails.append(n)

        return len(tails)

