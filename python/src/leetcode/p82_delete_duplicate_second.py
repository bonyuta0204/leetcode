from utils import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        result_head = ListNode(None)
        result_tail = result_head
        current = head
        prev = ListNode(None)
        next = head.next or ListNode(None)


        while current:
            prev_diff = current.val != prev.val
            next_diff = (not next) or current.val != next.val


            if prev_diff and next_diff:
                result_tail.next = ListNode(current.val)
                result_tail = result_tail.next
            prev = current
            current = current.next
            next = next.next or ListNode(None)

        return result_head.next

