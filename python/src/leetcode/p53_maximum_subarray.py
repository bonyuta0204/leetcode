from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        We can know the answer at n-th if we know the answer for n - 1.
        the largest maxSubArray which end at poistion n is either Result(n-1) + n or N
        """
        highest_num = [0 for _ in nums]

        if len(nums) == 0:
            return 0

        for i, n in enumerate(nums):
            if i == 0:
                highest_num[i] = n
            else:
                last_highest = highest_num[i-1]
                if last_highest > 0:
                    highest_num[i] = n + last_highest
                else:
                    highest_num[i] = n
        return max(highest_num)
