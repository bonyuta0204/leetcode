from typing import Optional
from leetcode.utils import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()

        while head is not None:
            if head in visited:
                return head
            else:
                visited.add(head)
                head = head.next
        return None
