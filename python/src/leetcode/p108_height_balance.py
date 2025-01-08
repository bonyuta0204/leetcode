from .utils import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        We can solve this recursively.

        for example, given array, 
        [-10, -1, 0, 1, 9]

        select middle (0) and make it top node.
        then create balanced tree for both left side ([-10, -1]) and right side([1, 9])
        """

        if not nums:
            return None

        center_idx = len(nums) // 2

        left_remaining = nums[:center_idx]
        right_remaining = nums[center_idx + 1:]

        return TreeNode(nums[center_idx], self.sortedArrayToBST(left_remaining), self.sortedArrayToBST(right_remaining))

