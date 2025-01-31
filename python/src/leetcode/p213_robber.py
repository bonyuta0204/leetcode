from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        # max_rob[i] indicate the max robbery amount upuntil house i
        # when rob first house
        max_rob_with_first = [0 for n in nums]

        # when rob first
        max_rob_without_first = [0 for n in nums]


        for i in range(len(nums) - 1):
            if i == 0:
                max_rob_with_first[i] = nums[i]
            elif i == 1:
                max_rob_with_first[i] = 0
            elif i == 2:
                max_rob_with_first[i] = max_rob_with_first[i - 2] + nums[i]
            else:
                max_rob_with_first[i] = max(max_rob_with_first[i - 2], max_rob_with_first[i - 3]) + nums[i]

        for i in range(len(nums)):
            if i == 0:
                max_rob_without_first[i] = 0
            elif i == 1:
                max_rob_without_first[i] = nums[i]
            elif i == 2:
                max_rob_without_first[i] = max_rob_without_first[i - 2] + nums[i]
            else:
                max_rob_without_first[i] = max(max_rob_without_first[i - 2], max_rob_without_first[i - 3]) + nums[i]

        return max(max_rob_with_first + max_rob_without_first)


