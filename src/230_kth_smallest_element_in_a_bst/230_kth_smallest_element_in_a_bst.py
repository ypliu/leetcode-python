# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        if (k < 1) or (not root):
            return None
        return self.kthSmallestInOrderTraversal(root, k)

    def kthSmallestInOrderTraversal(self, root, k):
        i = 0
        stack = []; temp = root
        while stack or temp:
            while temp:
                stack.append(temp)
                temp = temp.left
            temp = stack.pop()
            i += 1
            if (i == k):
                return temp.val
            #print temp.val
            temp = temp.right
        return None

# debug
s = Solution()
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
print s.kthSmallest(root, 1)
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
print s.kthSmallest(root, 3)
