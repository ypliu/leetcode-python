# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(-1)
        pre = dummy; key = None; temp = head
        while temp:
            if key != temp.val:
                key = temp.val
                pre.next = ListNode(key); pre = pre.next
            temp = temp.next
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
tmp = ListNode(2)
tmp.next = None
l1 = tmp
tmp = ListNode(1)
tmp.next = l1
l1 = tmp
tmp = ListNode(1)
tmp.next = l1
l1 = tmp
s.printList(l1)
s.printList(s.deleteDuplicates(l1))
tmp = ListNode(3)
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
tmp = ListNode(1)
tmp.next = l1
l1 = tmp
s.printList(l1)
s.printList(s.deleteDuplicates(l1))
