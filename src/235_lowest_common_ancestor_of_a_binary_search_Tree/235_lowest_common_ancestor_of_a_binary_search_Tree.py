# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if (not root):
            return None
        elif (p == q):
            return p
        if (p.val > q.val):
            p,q = q,p
        while root:
            if (q.val < root.val):
                root = root.left
            elif (p.val > root.val):
                root = root.right
            else:
                return root
        # should not be here
        return None

# debug
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
s = Solution()
print s.lowestCommonAncestor(root, root.left, root.right).val
print s.lowestCommonAncestor(root, root.left, root.left.right).val
