# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return
        node_res = TreeNode(root.val)
        self.maxPathSumRecursion(root, node_res)
        return node_res.val

    def maxPathSumRecursion(self, root, node_res):
        if not root:
            return 0
        max_sum_left = max(self.maxPathSumRecursion(root.left, node_res), 0)
        max_sum_right = max(self.maxPathSumRecursion(root.right, node_res), 0)
        node_res.val = max(max_sum_left+max_sum_right+root.val, node_res.val)
        return (max(max_sum_left, max_sum_right) + root.val)

# debug
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
s = Solution()
print s.maxPathSum(root)

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s = Solution()
print s.maxPathSum(root)
