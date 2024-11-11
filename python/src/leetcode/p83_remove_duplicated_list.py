from typing import Optional
from leetcode.utils import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edit the list in-place
        node = head

        while node is not None:
            next_node = node.next

            if next_node is None:
                break
            elif node.val == next_node.val:
                # bypass next_node since it is duplicated
                node.next = next_node.next
            else:
                # when next is not duplicated
                node = next_node
        return head
