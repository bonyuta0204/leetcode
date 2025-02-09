from typing import Optional
from .utils import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        We use recursive approach to merge tree TreeNode
        """

        if root1 and root2:
            return TreeNode(root1.val + root2.val, self.mergeTrees(root1.left, root2.left),  self.mergeTrees(root1.right, root2.right))
        elif root1:
            return root1
        elif root2:
            return root2
        else:
            return None
