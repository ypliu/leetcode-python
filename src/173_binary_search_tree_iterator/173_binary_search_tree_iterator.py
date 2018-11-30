# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return (len(self.stack) > 0)

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        val = node.val
        node = node.right
        while node:
            self.stack.append(node)
            node = node.left
        return val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

# debug
root = TreeNode(20)
root.left = TreeNode(1)
root.left.left = TreeNode(-10)
root.left.right = TreeNode(10)
root.right = TreeNode(300)
root.right.left = TreeNode(100)
root.right.right = TreeNode(500)
i, v = BSTIterator(root), []
while i.hasNext():
    v.append(i.next())
print v
