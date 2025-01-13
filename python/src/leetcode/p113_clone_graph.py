"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
from utils import Node


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        # Dictionary to map original nodes to their clones
        cloned = {}

        # Initialize the queue with the first node
        queue = deque([node])

        # Create a clone for the starting node
        cloned[node] = Node(node.val)

        # Perform BFS
        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:
                # If the neighbor hasn't been cloned yet, create the clone and enqueue the original
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # Add the cloned neighbor to the current node's clone
                cloned[current].neighbors.append(cloned[neighbor])

        # Return the clone of the original input node
        return cloned[node]
