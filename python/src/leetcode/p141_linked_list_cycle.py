from typing import Optional
from leetcode.utils import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # store node which is already visited
        visited = set()

        while True:
            if head is None:
                return False
            elif head in visited:
                return True
            else:
                visited.add(head)
                head = head.next
