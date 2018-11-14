# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(-1)
        temp = head
        while temp:
            pre = dummy; cur = dummy.next
            while cur and cur.val <= temp.val:
                pre = cur
                cur = cur.next
            pre.next = temp
            temp = temp.next
            pre.next.next = cur
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
tmp = ListNode(3)
l1 = tmp
tmp = ListNode(1)
tmp.next = l1
l1 = tmp
tmp = ListNode(2)
tmp.next = l1
l1 = tmp
tmp = ListNode(4)
tmp.next = l1
l1 = tmp
s.printList(l1)
l1 = s.insertionSortList(l1)
s.printList(l1)

tmp = ListNode(0)
l1 = tmp
tmp = ListNode(4)
tmp.next = l1
l1 = tmp
tmp = ListNode(3)
tmp.next = l1
l1 = tmp
tmp = ListNode(5)
tmp.next = l1
l1 = tmp
tmp = ListNode(-1)
tmp.next = l1
l1 = tmp
s.printList(l1)
l1 = s.insertionSortList(l1)
s.printList(l1)
