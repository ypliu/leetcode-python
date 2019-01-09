# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        if (not root):
            return []
        paths = []; q = [(root, str(root.val))]
        while q:
            node,p = q.pop(0)
            if (not node.left) and (not node.right):
                paths.append(p)
                continue
            if node.left:
                q.append((node.left, p+"->"+str(node.left.val)))
            if node.right:
                q.append((node.right, p+"->"+str(node.right.val)))                
        return paths

# debug
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
s = Solution()
print s.binaryTreePaths(root)
