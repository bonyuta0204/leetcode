from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # max_rob[i] indicate the max robbery amount upuntil house i
        max_rob = []

        for i in range(len(nums)):
            if i < 2:
                max_rob.append(nums[i])
            elif i == 2:
                max_rob.append(max_rob[0] + nums[i])
            else:
                max_rob.append(max(max_rob[i - 2], max_rob[i - 3]) + nums[i] )

        return max(max_rob)
