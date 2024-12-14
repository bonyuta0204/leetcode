from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        if len(nums) == 0:
            return 0

        for n in nums:
            for i, tail in enumerate(tails):
                if n <= tail:
                    tails[i] = n
                    break
            if len(tails) == 0 or n > tails[-1]:
                tails.append(n)

        return len(tails)

