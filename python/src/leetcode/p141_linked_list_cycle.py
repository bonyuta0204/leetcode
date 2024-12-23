from typing import Optional
from leetcode.utils import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # store node which is already visited
        visited = set()

        while head is not None:
            if head in visited:
                return True
            else:
                visited.add(head)
                head = head.next
        return False
