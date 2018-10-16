# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        #return self.isSameTreeRecursion(p, q)
        return self.isSameTreePreorderStack(p, q)

    def isSameTreeRecursion(self, p, q):
        if not p or not q:
            return p == q
        elif p.val == q.val:
            return self.isSameTreeRecursion(p.left, q.left) and self.isSameTreeRecursion(p.right, q.right)
        return False

    def isSameTreePreorderStack(self, p, q):
        stack=[(p,q)]
        while stack:
            st1, st2 = stack.pop()
            if not st1 and not st2:
                continue
            elif not st1 or not st2:
                return False
            elif st1.val == st2.val:
                stack.append((st1.left, st2.left))
                stack.append((st1.right, st2.right))
            else:
                return False
        return True

# debug
s = Solution()
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
print s.isSameTree(p, q)

p = TreeNode(1)
p.left = TreeNode(2)
q = TreeNode(1)
q.right = TreeNode(2)
print s.isSameTree(p, q)

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(1)
q = TreeNode(1)
q.left = TreeNode(1)
q.right = TreeNode(2)
print s.isSameTree(p, q)
