# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        sum_head = ListNode(0)
        sum_tail = sum_head
        carry = 0

        while l1 or l2:
            sum_val = carry

            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next

            if sum_val >= 10:
                carry = 1
                sum_val -= 10
            else:
                carry = 0

            sum_tail.next = ListNode(sum_val)
            sum_tail = sum_tail.next

        if carry == 1:
            sum_tail.next = ListNode(1)

        return sum_head.next



