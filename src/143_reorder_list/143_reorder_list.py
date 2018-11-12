# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next; slow.next = None; dummy = None
        while temp:
            tt2 = temp.next
            temp.next = dummy
            dummy = temp
            temp = tt2
        temp = dummy; slow = head
        while temp:
            dummy = temp.next
            temp.next = slow.next
            slow.next = temp
            slow = temp.next
            temp = dummy

# debug
    def printList(self, head):
        while head != None:
            print head.val,
            head = head.next
            if head != None:
                print '->',
            else:
                print

l1 = ListNode(5)
tmp = ListNode(4)
tmp.next = l1
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
s.reorderList(l1)
s.printList(l1)
