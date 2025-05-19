# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode()
        current = head
        carry = 0

        while l1 or l2:
            if l1 is not None:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
            if l2 is not None:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0

            total = l1_val + l2_val + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

        if carry:
            current.next = ListNode(carry)

        return head.next
