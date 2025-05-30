# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insert(self, head, value):
        """
        input: ListNode head, int value
        return: ListNode
        """
        # write your solution here
        newNode = ListNode(value)

        if head is None or head.value >= value:
            newNode.next = head
            return newNode

        prev = head
        while prev.next is not None and prev.next.value < value:
            prev = prev.next

        newNode.next = prev.next
        prev.next = newNode

        return head


