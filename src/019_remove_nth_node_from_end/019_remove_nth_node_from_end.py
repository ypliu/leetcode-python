# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # With the help of added head pointer dummy, avoid the negative impact on deleting the possible first element
        dummy = ListNode(-100)
        dummy.next = head
        fast = dummy
        slow = dummy

        for i in range(n):
            fast = fast.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next

    def printList(self, head):
        while head != None:
            print head.val
            head = head.next

#
s = Solution()

tmp = ListNode(5)
tmp.next = None
head = tmp
tmp = ListNode(4)
tmp.next = head
head = tmp
tmp = ListNode(3)
tmp.next = head
head = tmp
tmp = ListNode(2)
tmp.next = head
head = tmp
tmp = ListNode(1)
tmp.next = head
head = tmp

s.printList(head)
s.removeNthFromEnd(head, 2)
s.printList(head)
