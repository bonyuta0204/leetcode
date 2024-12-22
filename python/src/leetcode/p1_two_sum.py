from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        we store the subtraction from target.
        if we find current nums in the key of the store, it is solved
        """

        subtraction_map = {}

        for i, n in enumerate(nums):

            if n in subtraction_map:
                return [subtraction_map[n], i]
            else:
                subtraction_map[target - n] = i

        # never reaches here from the input assumption
        return []
