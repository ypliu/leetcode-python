# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # if -1 == self.computeHeightRecursion(root):
        if -1 == self.computeHeightStack(root):
            return False
        return True

    def computeHeightRecursion(self, root):
        if not root:
            return 0
        hl = self.computeHeightRecursion(root.left)
        if -1 == hl:
            return -1
        hr = self.computeHeightRecursion(root.right)
        if -1 == hr or abs(hl - hr) > 1:
            return -1
        return max(hl, hr)+1

    def computeHeightStack(self, root):
        stack = []; temp = root
        last = None; depths = {}
        depths[None] = 0
        # PostorderTraversal
        while stack or temp:
            while temp:
                stack.append(temp)
                temp = temp.left
            temp = stack[-1]
            if not temp.right or last == temp.right:
                stack.pop()
                hl, hr = depths[temp.left], depths[temp.right]
                if abs(hl - hr) > 1:
                    return -1
                depths[temp] = max(hl,hr) + 1
                last, temp = temp, None
            else:
                temp = temp.right
        return depths[root]

# debug
s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print s.isBalanced(root)

root = TreeNode(1)
root.left = TreeNode(21)
root.right = TreeNode(22)
root.left.left = TreeNode(31)
root.left.right = TreeNode(32)
root.left.left.left = TreeNode(41)
root.left.left.right = TreeNode(42)
print s.isBalanced(root)
