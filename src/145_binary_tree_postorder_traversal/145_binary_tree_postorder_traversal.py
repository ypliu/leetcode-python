# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        return self.postorderTraversalIteration(root)
        res = []
        self.postorderTraversalRecursion(root, res)
        return res

    def postorderTraversalIteration(self, root):
        if not root:
            return []
        res = []; post_stack = [root]
        while post_stack:
            temp = post_stack.pop()
            res.append(temp.val)
            if temp.left:
                post_stack.append(temp.left)
            if temp.right:
                post_stack.append(temp.right)
        return res[::-1]

    def postorderTraversalRecursion(self, root, res):
        if not root:
            return
        self.postorderTraversalRecursion(root.left, res)
        self.postorderTraversalRecursion(root.right, res)
        res.append(root.val)

# debug
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
s = Solution()
print s.postorderTraversal(root)
