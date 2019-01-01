# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if (not head):
            return True
        return self.isPalindromeConstSpace(head)
        return self.isPalindromeBasedList(head)

    def isPalindromeConstSpace(self, head):
        slow = fast = head; prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        if fast:  # odd number of nodes in list
            slow = slow.next
        while prev and (prev.val == slow.val):
            slow = slow.next
            prev = prev.next
        return (not prev)

    def isPalindromeBasedList(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        half_len = len(res) >> 1
        return (res[:half_len] == res[:len(res)-half_len-1:-1])

# debug
s = Solution()
tmp = ListNode(2)
l1 = tmp
tmp = ListNode(1)
tmp.next = l1
l1 = tmp
print s.isPalindrome(l1)

tmp = ListNode(1)
l1 = tmp
tmp = ListNode(2)
tmp.next = l1
l1 = tmp
tmp = ListNode(2)
tmp.next = l1
l1 = tmp
tmp = ListNode(1)
tmp.next = l1
l1 = tmp
print s.isPalindrome(l1)
