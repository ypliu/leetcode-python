# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if k <= 0 or not head:
            return head

        slow = fast = head; i = 0
        while fast and i < k:
            i += 1
            fast = fast.next
        if not fast:
            k %= i
            if 0 == k:
                return head
            fast = head
            while k > 0:
                k -= 1
                fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = head
        head = slow.next
        slow.next = None
        return head

# debug
    def printList(self, head):
        while head != None:
            print head.val,
            head = head.next
            if head != None:
                print '->',
            else:
                print

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
s = Solution()
s.printList(l1)
s.printList(s.rotateRight(l1, 2))
tmp = ListNode(2)
tmp.next = None
l1 = tmp
tmp = ListNode(1)
tmp.next = l1
l1 = tmp
tmp = ListNode(0)
tmp.next = l1
l1 = tmp
s = Solution()
s.printList(l1)
s.printList(s.rotateRight(l1, 4))
