# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        dummy = ListNode(-1)
        dummy.next = head
        prev,cur = dummy,head
        while cur != None:
            if (val == cur.val):
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next

# debug
    def printList(self, head):
        while head != None:
            print head.val,
            head = head.next
            if head != None:
                print '->',
            else:
                print

s = Solution()
tmp = ListNode(6)
l1 = tmp
tmp = ListNode(5)
tmp.next = l1
l1 = tmp
tmp = ListNode(4)
tmp.next = l1
l1 = tmp
tmp = ListNode(3)
tmp.next = l1
l1 = tmp
tmp = ListNode(6)
tmp.next = l1
l1 = tmp
tmp = ListNode(2)
tmp.next = l1
l1 = tmp
tmp = ListNode(1)
tmp.next = l1
l1 = tmp
s.printList(l1)
l1 = s.removeElements(l1, 6)
s.printList(l1)
