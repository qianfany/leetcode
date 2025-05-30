# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def merge(self, one, two):
        """
        input: ListNode one, ListNode two
        return: ListNode
        """
        # write your solution here
        dummy = ListNode(0)
        cur = dummy

        while one is not None and two is not None:
            if one.val < two.val:
                cur.next = one
                one = one.next
            else:
                cur.next = two
                two = two.next
            cur = cur.next

        cur.next = one if one is not None else two

        return dummy.next
