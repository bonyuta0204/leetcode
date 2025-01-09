from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        """
        basic idea is too traverse using BFS with level information.
        Then, we can switch the order by looking at the level
        """

        queue = deque([(0, root)])

        result = []

        while queue:
            level, node = queue.popleft()

            if not node:
                continue

            if len(result) > level:

                result[level].append(node.val)
            else:
                result.append([node.val])

            # 0-indexの偶数階層は、右から
            if level % 2 == 0:
                queue.append((level + 1, node.right))
                queue.append((level + 1, node.left))

            # 奇数階層は左から
            else:
                queue.append((level + 1, node.left))
                queue.append((level + 1, node.right))
        return result


