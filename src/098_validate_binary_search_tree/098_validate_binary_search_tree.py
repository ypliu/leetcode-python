# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.isValidSubBST(root, -float('inf'), float('inf'))

    def isValidSubBST(self, subbst, min, max):
        if not subbst:
            return True
        if subbst.val <= min:
                return False
        if subbst.val >= max:
                return False
        return self.isValidSubBST(subbst.left, min, subbst.val) and self.isValidSubBST(subbst.right, subbst.val, max)

# debug
s = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print s.isValidBST(root)
temp = TreeNode(4)
temp.left = TreeNode(3)
temp.right = TreeNode(6)
root = TreeNode(5)
root.left = TreeNode(1)
root.right = temp
print s.isValidBST(root)
