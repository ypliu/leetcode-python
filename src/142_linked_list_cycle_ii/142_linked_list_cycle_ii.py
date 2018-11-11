# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return slow
        return None

# debug
s = Solution()
head = temp = ListNode(0)
temp.next = ListNode(1)
temp = temp.next
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
temp.next = ListNode(9)
temp = temp.next
temp.next = loop
print s.detectCycle(head).val

head = temp = ListNode(3)
loop = temp.next = ListNode(2)
temp = temp.next
temp.next = ListNode(0)
temp = temp.next
temp.next = ListNode(-4)
temp = temp.next
temp.next = loop
print s.detectCycle(head).val
