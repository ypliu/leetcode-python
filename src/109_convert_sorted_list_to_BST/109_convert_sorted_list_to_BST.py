# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        return self.sortedListToBSTRecursion(head, None)

    def sortedListToBSTRecursion(self, head, tail):
        if head == tail:
            return None
        elif head.next == tail:
            return TreeNode(head.val)
        slow = fast = head
        while (fast != tail) and (fast.next != tail):
            fast = fast.next.next
            slow = slow.next
        root = TreeNode(slow.val)
        root.left = self.sortedListToBSTRecursion(head, slow)
        root.right = self.sortedListToBSTRecursion(slow.next, tail)
        return root

# debug
    def printList(self, head):
        while head != None:
            print head.val,
            head = head.next
            if head != None:
                print '->',
            else:
                print

    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            queue_temp = []; val_temp = []
            for node in queue:
                val_temp.append(node.val)
                if node.left:
                    queue_temp.append(node.left)
                if node.right:
                    queue_temp.append(node.right)
            queue = queue_temp
            res.append(val_temp)
        return res

lst = ListNode(9)
tmp = ListNode(5)
tmp.next = lst
lst = tmp
tmp = ListNode(0)
tmp.next = lst
lst = tmp
tmp = ListNode(-3)
tmp.next = lst
lst = tmp
tmp = ListNode(-10)
tmp.next = lst
lst = tmp
s = Solution()
s.printList(lst)
root = s.sortedListToBST(lst)
print s.levelOrder(root)
