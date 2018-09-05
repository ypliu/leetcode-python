from Queue import PriorityQueue

# as same as Recursion version, both O(N*log^k)

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

        pq = PriorityQueue()
        for i in lists:
            if i:
                pq.put((i.val, i))

        head = temp = ListNode(0)
        while not pq.empty():
            val, node = pq.get()
            temp.next = ListNode(val)
            temp = temp.next
            node = node.next
            if node:
                pq.put((node.val, node))

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

temp = ListNode(5)
temp.next = None
l1 = temp
temp = ListNode(4)
temp.next = l1
l1 = temp
temp = ListNode(1)
temp.next = l1
l1 = temp

temp = ListNode(4)
temp.next = None
l2 = temp
temp = ListNode(3)
temp.next = l2
l2 = temp
temp = ListNode(1)
temp.next = l2
l2 = temp

temp = ListNode(6)
temp.next = None
l3 = temp
temp = ListNode(2)
temp.next = l3
l3 = temp

lists = []
lists.append(l1)
lists.append(l2)
lists.append(l3)

s = Solution()
for i in lists:
    s.printList(i)
s.printList(s.mergeKLists(lists))
