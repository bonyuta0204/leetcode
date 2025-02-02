# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while slow and fast:
            slow = slow.next

            fast = fast.next
            if fast:
                fast = fast.next

            # cycle detected
            if slow and slow == fast:

                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow
        return None
