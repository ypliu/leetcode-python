# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if m < 1 or m >= n or not head:
            return head

        dummy = ListNode(-1); dummy.next = head
        pre = dummy; i = 1
        while i < m and pre.next:
            pre = pre.next
            i += 1
        if i < m:
            print "Error, 'm' is less than the length of list 'head'!"
            return head
        last = pre.next; temp = pre.next; pre.next = None
        while i <= n and temp:
            temp2 = temp
            temp = temp.next
            temp2.next = pre.next
            pre.next = temp2
            i += 1
        if i <= n:
            print "Error, 'n' is more than the length of list 'head'!"
            return head
        last.next = temp
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
tmp = ListNode(5)
tmp.next = None
l1 = tmp
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
s.printList(l1)
s.printList(s.reverseBetween(l1, 2, 4))
