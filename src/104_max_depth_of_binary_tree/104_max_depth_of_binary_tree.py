# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        depth = 0
        queue = [root]
        while queue:
            depth += 1
            queue_temp = []
            for node in queue:
                if node.left:
                    queue_temp.append(node.left)
                if node.right:
                    queue_temp.append(node.right)
            queue = queue_temp
        return depth

# debug
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s = Solution()
print s.maxDepth(root)
