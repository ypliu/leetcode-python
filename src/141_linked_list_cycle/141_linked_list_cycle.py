# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return False
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# debug
s = Solution()
head = temp = ListNode(1)
temp.next = ListNode(2)
temp = temp.next
temp.next = ListNode(3)
temp = temp.next
temp.next = ListNode(4)
temp = temp.next
temp.next = ListNode(5)
temp = temp.next
temp.next = ListNode(6)
temp = temp.next
temp.next = ListNode(7)
temp = temp.next
temp.next = ListNode(8)
temp = temp.next
print s.hasCycle(head)

head = temp = ListNode(1)
temp.next = ListNode(2)
temp = temp.next
temp.next = ListNode(3)
temp = temp.next
temp.next = ListNode(4)
temp = temp.next
temp.next = ListNode(5)
temp = temp.next
loop = temp.next = ListNode(6)
temp = temp.next
temp.next = ListNode(7)
temp = temp.next
temp.next = ListNode(8)
temp = temp.next
temp.next = loop
print s.hasCycle(head)
