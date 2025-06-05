class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, target):
        if head is None or head.next is None:
            return head

        small = ListNode(0)
        large = ListNode(0)
        curSmall = small
        curLarge = large

        while head:
            if head.val < target:
                curSmall.next = head
                curSmall = curSmall.next
            else:
                curLarge.next = head
                curLarge = curLarge.next
            head = head.next

            curSmall.next = large.next
            curLarge.next = None

        return small.next
