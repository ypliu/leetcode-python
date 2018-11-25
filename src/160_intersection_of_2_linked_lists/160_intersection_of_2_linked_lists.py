# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if (not headA) or (not headB):
            return None
        temp1,temp2 = headA,headB
        while temp1 != temp2:
            temp1 = temp1.next if temp1 else headB
            temp2 = temp2.next if temp2 else headA
        return temp1

# debug
headA = temp = ListNode(11)
temp.next = ListNode(12)
temp = temp.next
temp.next = p = ListNode(31)
temp = temp.next
temp.next = ListNode(32)
temp = temp.next
temp.next = ListNode(33)
headB = temp = ListNode(21)
temp.next = ListNode(22)
temp = temp.next
temp.next = ListNode(23)
temp = temp.next
temp.next = p
s = Solution()
p = s.getIntersectionNode(headA, headB)
print p.val
