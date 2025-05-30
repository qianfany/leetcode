# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorder(self, head):
        """
        input: ListNode head
        return: ListNode
        """
        # write your solution here
        if head is None or head.next is None:
            return head

        mid = self.findMiddle(head)
        two = mid.next
        mid.next = None

        two = self.reverse(two)
        return self.merge(head, two)

    def findMiddle(self, head):
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        prev = None
        while head is not None:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

    def merge(self, one, two):
        dummy = ListNode(0)
        cur = dummy
        while one is not None and two is not None:
            cur.next = one
            one = one.next
            cur = cur.next

            cur.next = two
            two = two.next
            cur = cur.next

        cur.next = one if one is not None else two
        return dummy.next


