# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def numberOfNodes(self, head):
        """
        input: ListNode head
        return: int
        """
        if head is None:
            return 0
        res = 0
        while head:
            head = head.next
            res += 1
        return res

