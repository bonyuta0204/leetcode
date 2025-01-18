class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Given an array of positive integers nums and a positive integer target, return the minimal length of a 
        subarray
         whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
        """

        if not nums:
            return 0
        start_idx = 0
        end_idx = 0
        current_sum = nums[0]
        min_len = None

        while True:
            if current_sum < target:
                end_idx += 1
                if end_idx < len(nums):
                    current_sum += nums[end_idx]
                else:
                    break
            else:
                current_len = end_idx - start_idx + 1
                if not min_len or current_len < min_len:
                    min_len = current_len

                current_sum -= nums[start_idx]
                start_idx += 1
        return min_len or 0



