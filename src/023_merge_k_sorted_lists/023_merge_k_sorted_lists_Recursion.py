# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        num_lists = len(lists)
        if num_lists == 0:
            return None
        elif num_lists == 1:
            return lists[0]
        elif num_lists == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            mid = num_lists // 2
            l1 = self.mergeKLists(lists[:mid])
            l2 = self.mergeKLists(lists[mid:])
            return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1

        head = ListNode(0)
        temp = head

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        if l1 != None:
            temp.next = l1
        else:
            temp.next = l2

        return head.next

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
tmp = ListNode(1)
tmp.next = l1
l1 = tmp

tmp = ListNode(4)
tmp.next = None
l2 = tmp
tmp = ListNode(3)
tmp.next = l2
l2 = tmp
tmp = ListNode(1)
tmp.next = l2
l2 = tmp

tmp = ListNode(6)
tmp.next = None
l3 = tmp
tmp = ListNode(2)
tmp.next = l3
l3 = tmp

lists = []
lists.append(l1)
lists.append(l2)
lists.append(l3)

s = Solution()
for i in lists:
    s.printList(i)
s.printList(s.mergeKLists(lists))
