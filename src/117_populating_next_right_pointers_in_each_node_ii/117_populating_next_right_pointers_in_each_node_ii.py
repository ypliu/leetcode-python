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
        self.connectIteration(root)

    def connectIteration(self, root):
        cur = root
        dummy = TreeLinkNode(-1)
        while cur:
            dummy.next = None; temp = dummy
            while cur:
                if cur.left:
                    temp.next = cur.left
                    temp = cur.left
                if cur.right:
                    temp.next = cur.right
                    temp = cur.right
                cur = cur.next
            cur = dummy.next

# debug
root = TreeLinkNode(1)
root.left =  TreeLinkNode(2)
root.right = TreeLinkNode(3)
root.left.left =  TreeLinkNode(4)
root.left.right =  TreeLinkNode(5)
root.right.right =  TreeLinkNode(7)
s = Solution()
s.connect(root)
