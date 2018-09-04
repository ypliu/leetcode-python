# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:
            return l2
        elif not l2:
            return l1

        head = ListNode(0)
        temp = head

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        if l1 != None:
            temp.next = l1
        else:
            temp.next = l2

        return head.next

    def printList(self, head):
        while head != None:
            print head.val,
            head = head.next
            if head != None:
                print '->',
            else:
                print

# debug
tmp = ListNode(4)
tmp.next = None
l1 = tmp
tmp = ListNode(2)
tmp.next = l1
l1 = tmp
tmp = ListNode(1)
tmp.next = l1
l1 = tmp

tmp = ListNode(4)
tmp.next = None
l2 = tmp
tmp = ListNode(3)
tmp.next = l2
l2 = tmp
tmp = ListNode(1)
tmp.next = l2
l2 = tmp

s = Solution()
s.printList(l1)
s.printList(l2)
s.printList(s.mergeTwoLists(l1, l2))
