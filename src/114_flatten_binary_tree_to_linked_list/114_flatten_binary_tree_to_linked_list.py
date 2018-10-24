# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        if not root:
            return
        # self.flattenRecursion(root, None)
        self.flattenIteration(root)

    def flattenRecursion(self, root, subtree):
        if root.right:
            self.flattenRecursion(root.right, subtree)
        else:
            root.right = subtree
        if root.left:
            self.flattenRecursion(root.left, root.right)
            root.right = root.left
            root.left = None

    def flattenIteration(self, root):
        while root:
            if root.left:
                if root.right:
                    temp = root.left
                    while temp.right:
                        temp = temp.right
                    temp.right = root.right
                root.right = root.left
                root.left = None
            root = root.right

# debug

    def isValid(self, root):
        while root:
            print root.val, "->",
            if root.left:
                print "Error!"
                return
            root = root.right
        print

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
s = Solution()
s.flatten(root)
s.isValid(root)
