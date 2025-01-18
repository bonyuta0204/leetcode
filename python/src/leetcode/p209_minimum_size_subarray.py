class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Given an array of positive integers nums and a positive integer target, return the minimal length of a 
        subarray
         whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
        """
        left, total = 0, 0

        min_len = float("inf")

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                min_len = min(right - left + 1, min_len)

                total -= nums[left]
                left += 1

        return 0 if min_len == float("inf") else  min_len


