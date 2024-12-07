
from typing import Optional
from utils import TreeNode
from collections import deque

class Solution:
    def minDepth(self, root:Optional[TreeNode] ) -> int:
        """
        We use bfs to search tree and return the depth if both edge is None
        """

        if root is None:
            return 0

        queue = deque()

        queue.append((root, 1))

        while len(queue) > 0:
            node, depth = queue.popleft()

            if node.left is None and node.right is None:
                # found leaf
                return depth
            if node.left is not None:
                queue.append((node.left, depth + 1))
            if node.right is not None:
                queue.append((node.right, depth + 1))

        return 0
