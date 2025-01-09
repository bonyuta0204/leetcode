from utils import TreeNode
from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        We can use recursion to solve this problem.
        given a node, solve two sub-problem for each child nodes
        """

        def is_leaf(node):
            if node.left:
                return False
            if node.right:
                return False
            return True

        if root:
            if is_leaf(root) and root.val == targetSum:
                return True
            return self.hasPathSum(root.left,  targetSum - root.val) or self.hasPathSum(root.right,  targetSum - root.val)
        else:
            return False

