from utils import ListNode
from typing import List, Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = None
        current =  head

        while current:
            # temporaly memorize next node
            next = current.next
            current.next = prev

            prev = current
            if next:
                current = next
            else:
                 break
        return current

