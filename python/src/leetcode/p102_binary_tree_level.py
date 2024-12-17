from typing import Optional
from collections import deque
from utils import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]):
        """
        Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

        Solution:
            Basic idea ia BFS, traversaling from shallower node.
            with traversal, build result set iteratively
        """

        queue = deque([(root, 0)])
        results = []

        while queue:
            target_node, level = queue.popleft()

            if target_node:
                if len(results) > level:
                     results[level].append(target_node.val)
                else:
                    results.append([target_node.val])

                queue.append((target_node.left, level + 1))
                queue.append((target_node.right, level + 1))
        return results






