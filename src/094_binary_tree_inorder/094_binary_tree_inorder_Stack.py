# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        return self.inorderTraversalStack(root)

    def inorderTraversalStack(self, root):
        temp = root
        res = []; stack = []
        while temp or stack:
            while temp:
                stack.append(temp)
                temp = temp.left
            temp = stack.pop()
            res.append(temp.val)
            temp = temp.right
        return res

# debug
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
s = Solution()
print s.inorderTraversal(root)
