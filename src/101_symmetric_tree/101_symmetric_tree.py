# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True
        # return self.isMirrorRecursion(root.left, root.right)
        return self.isMirrorIteration(root)

    def isMirrorRecursion(self, subtree1, subtree2):
        if not subtree1 or not subtree2:
            return subtree1 == subtree2
        elif subtree1.val == subtree2.val:
            return self.isMirrorRecursion(subtree1.left, subtree2.right) and self.isMirrorRecursion(subtree1.right, subtree2.left)
        return False

    def isMirrorIteration(self, root):
        if not root:
            return True
        queue = []
        queue.insert(0, (root.left, root.right))
        while(queue):
            node_l, node_r = queue.pop()
            if not node_l and not node_r:
                continue
            elif not node_l or not node_r:
                return False
            elif node_l.val != node_r.val:
                return False
            queue.insert(0, (node_l.left, node_r.right))
            queue.insert(0, (node_r.left, node_l.right))
        return True

# debug
s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
print s.isSymmetric(root)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)
print s.isSymmetric(root)
