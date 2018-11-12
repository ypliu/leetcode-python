# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        return self.preorderTraversalIteration(root)
        return self.preorderTraversalIteration2(root)
        res = []
        self.preorderTraversalRecursion(root, res)
        return res

    def preorderTraversalIteration(self, root):
        res = []
        pre_stack = []; temp = root
        while pre_stack or temp:
            while temp:
                res.append(temp.val)
                pre_stack.append(temp)
                temp = temp.left
            temp = pre_stack.pop().right
        return res

    def preorderTraversalIteration2(self, root):
        if not root:
            return []
        res = []; pre_stack = [root]
        while pre_stack:
            temp = pre_stack.pop()
            res.append(temp.val)
            if temp.right:
                pre_stack.append(temp.right)
            if  temp.left:
                pre_stack.append(temp.left)
        return res

    def preorderTraversalRecursion(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.preorderTraversalRecursion(root.left, res)
        self.preorderTraversalRecursion(root.right, res)

# debug
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
s = Solution()
print s.preorderTraversal(root)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print s.preorderTraversal(root)
