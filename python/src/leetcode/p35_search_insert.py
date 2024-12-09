from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            self.render(nums, left, right)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    def render(self,nums,left, right):
        #
        # 01 02 03 04
        #  l        r

        main_line =  " ".join(["%2d" % n for n in nums])
        sub_line = [" "] * len(main_line)

        sub_line[left * 3 + 1] = "L"
        sub_line[right * 3 + 1] = "R"

        print(main_line)
        print("".join(sub_line))
        print("------")



if __name__ == "__main__":
    Solution().searchInsert([1, 2, 5, 6, 9, 12, 15, 16, 19, 21, 24, 28, 29, 45, 58], 24)
