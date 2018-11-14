# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        return self.mergeSortForList(head)

    def mergeSortForList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(-1); dummy.next = head
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        list1, list2 = head, slow.next
        slow.next = None
        list1 = self.mergeSortForList(list1)
        list2 = self.mergeSortForList(list2)
        temp = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        temp.next = list1 if list1 else list2
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
tmp = ListNode(3)
l1 = tmp
tmp = ListNode(1)
tmp.next = l1
l1 = tmp
tmp = ListNode(2)
tmp.next = l1
l1 = tmp
tmp = ListNode(4)
tmp.next = l1
l1 = tmp
s.printList(l1)
l1 = s.sortList(l1)
s.printList(l1)

tmp = ListNode(0)
l1 = tmp
tmp = ListNode(4)
tmp.next = l1
l1 = tmp
tmp = ListNode(3)
tmp.next = l1
l1 = tmp
tmp = ListNode(5)
tmp.next = l1
l1 = tmp
tmp = ListNode(-1)
tmp.next = l1
l1 = tmp
s.printList(l1)
l1 = s.sortList(l1)
s.printList(l1)
