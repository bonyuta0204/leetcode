from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        we can use permutation for N length list from N-1 length list.
        N length permutation can by created by N times by inserting new element in all possible position.

        We can solve it resursively but,  we use iterative approach to avoid using too much stack memory
        """

        if len(nums) == 0:
            return [[]]

        result = [[]]

        for n in nums:
            new_result = []
            for r in result:
                # e.g r = [1, 2, 3]
                for p in range(len(r) + 1):
                    new_list = r.copy()
                    new_list.insert(p, n)
                    new_result.append(new_list)
            result = new_result

        return result

