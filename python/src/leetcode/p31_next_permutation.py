class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1)

        (2, 4, 1, 3)
        """

        # index of array where we have to increment to next number
        change_idx = 0

        for i in reversed(range(len(nums))):

            if i == 0:
                # edge case where this is the last element
                change_idx = -1

            if nums[i] > nums[i - 1]:
                change_idx = i - 1
                break
        print(f"{change_idx=}")

        if change_idx == -1:
            nums.sort()

        else:
            # swap the element with next bigger element

            next_bigger = float('inf')
            next_bigger_idx = 0
            for i in range(change_idx + 1,len(nums)):
                if nums[i] < next_bigger and nums[i] > nums[change_idx]:
                    next_bigger = nums[i]
                    next_bigger_idx = i
            nums[next_bigger_idx] = nums[change_idx]
            nums[change_idx] = next_bigger
            nums[change_idx+1:] = sorted(nums[change_idx+1:])








