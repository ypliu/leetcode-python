# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head
        pre_end = dummy

        while True:
            sub_list, i = pre_end.next, 0
            while sub_list and i < k:
                sub_list = sub_list.next
                i += 1
            # make sure there exist k elements in the rest of this segment
            if i < k:
                break
            else:
                cur_end = temp = pre_end.next
                for i in range(k):
                    fol = temp.next
                    temp.next = sub_list
                    sub_list = temp
                    temp = fol
                pre_end.next = sub_list
                pre_end = cur_end

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

tmp = ListNode(10)
tmp.next = None
l1 = tmp
tmp = ListNode(9)
tmp.next = l1
l1 = tmp
tmp = ListNode(8)
tmp.next = l1
l1 = tmp
tmp = ListNode(7)
tmp.next = l1
l1 = tmp
tmp = ListNode(6)
tmp.next = l1
l1 = tmp
tmp = ListNode(5)
tmp.next = l1
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
s.printList(s.reverseKGroup(l1, 3))
