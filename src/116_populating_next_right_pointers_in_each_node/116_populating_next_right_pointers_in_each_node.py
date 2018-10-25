# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        if not root:
            return
        # self.connectRecursion(root)
        self.connectIteration(root)

    def connectRecursion(self, root):
        if not root.left:
            return
        root.left.next = root.right
        self.connectRecursion(root.left)
        if root.next:
            root.right.next = root.next.left
        self.connectRecursion(root.right)

    def connectIteration(self, root):
        cur = root
        while cur.left:
            temp = cur.left
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            cur = temp

# debug
root = TreeLinkNode(1)
root.left =  TreeLinkNode(2)
root.right = TreeLinkNode(3)
root.left.left =  TreeLinkNode(4)
root.left.right =  TreeLinkNode(5)
root.right.left =  TreeLinkNode(6)
root.right.right =  TreeLinkNode(7)
s = Solution()
s.connect(root)
