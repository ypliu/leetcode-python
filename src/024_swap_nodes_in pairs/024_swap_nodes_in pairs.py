# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head

        while cur and cur.next:
            fol = cur.next
            pre.next = fol
            cur.next = fol.next
            fol.next = cur
            pre = cur
            cur = pre.next

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

tmp = ListNode(4)
tmp.next = None
l1 = tmp
tmp = ListNode(3)
tmp.next = l1
l1 = tmp
tmp = ListNode(2)
tmp.next = l1
l1 = tmp
tmp = ListNode(1)
tmp.next = l1
l1 = tmp

s = Solution()
s.printList(l1)
s.printList(s.swapPairs(l1))
