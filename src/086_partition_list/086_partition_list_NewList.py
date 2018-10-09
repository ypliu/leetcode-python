# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        dummy1 = ListNode(-1); dummy2 = ListNode(-2)
        pre1 = dummy1; pre2 = dummy2; temp = head
        while temp:
            if temp.val < x:
                pre1.next = ListNode(temp.val)
                pre1 = pre1.next
            else:
                pre2.next = ListNode(temp.val)
                pre2 = pre2.next
            temp = temp.next
        pre1.next = dummy2.next
        return dummy1.next

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
tmp = ListNode(2)
tmp.next = None
l1 = tmp
tmp = ListNode(5)
tmp.next = l1
l1 = tmp
tmp = ListNode(2)
tmp.next = l1
l1 = tmp
tmp = ListNode(3)
tmp.next = l1
l1 = tmp
tmp = ListNode(4)
tmp.next = l1
l1 = tmp
tmp = ListNode(1)
tmp.next = l1
l1 = tmp
s.printList(l1)
s.printList(s.partition(l1, 3))
