# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # BFS, it returns 'depth' once there is a leaf in queue
        if not root:
            return 0
        queue = [root]; depth = 1
        while queue:
            queue_temp = []
            for node in queue:
                if not node.left:
                    if not node.right:
                        return depth
                    else:
                        queue_temp.append(node.right)
                else:
                    queue_temp.append(node.left)
                    if node.right:
                        queue_temp.append(node.right)
            queue = queue_temp
            depth += 1

# debug
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s = Solution()
print s.minDepth(root)
