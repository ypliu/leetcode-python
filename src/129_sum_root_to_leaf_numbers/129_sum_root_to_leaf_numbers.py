# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        sum = 0
        queue = [(root, root.val)]
        while queue:
            queue_temp = []
            for node,val in queue:
                if node.left:
                    queue_temp.append((node.left, val*10 + node.left.val))
                    if node.right:
                        queue_temp.append((node.right, val*10 + node.right.val))
                else:
                    if node.right:
                        queue_temp.append((node.right, val*10 + node.right.val))
                    else:
                        sum += val
            queue = queue_temp
        return sum

# debug
s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print s.sumNumbers(root)

root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)
print s.sumNumbers(root)
