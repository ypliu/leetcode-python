# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if (not root):
            return root
        queue = [root]
        while queue:
            queue_temp = []
            for node in queue:
                node.left,node.right = node.right,node.left
                if node.left:
                    queue_temp.append(node.left)
                if node.right:
                    queue_temp.append(node.right)
            queue = queue_temp
        return root

# debug
    def printTreeByLayer(self, root):
        if (not root):
            return root
        queue = [root]
        while queue:
            queue_temp = []
            for node in queue:
                print node.val,
                if node.left:
                    queue_temp.append(node.left)
                if node.right:
                    queue_temp.append(node.right)
            print
            queue = queue_temp

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
s = Solution()
s.printTreeByLayer(root)
root = s.invertTree(root)
s.printTreeByLayer(root)
