# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if (None == root) or (None == p) or (None == q):
            return None
        elif (p == q):
            return p
        return self.lowestCommonAncestorIteration(root, p, q)

    def lowestCommonAncestorIteration(self, root, p, q):
        stack,lca_inx = [[root, 0]],0
        found_one = True if ((root == p) or (root == q)) else False
        while stack:
            node,flag = stack[-1]
            if (2 == flag):
                stack.pop()
                if (len(stack) == lca_inx):
                    lca_inx -= 1
            else:
                node_s = node.left if (0 == flag) else node.right
                stack[-1][1] += 1
                if node_s:
                    stack.append([node_s,0])
                    if (not found_one):
                        lca_inx += 1
                    if (node_s == p) or (node_s == q):
                        if found_one:
                            return stack[lca_inx][0]
                        else:
                            found_one = True
        return None

# debug
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
s = Solution()
print s.lowestCommonAncestor(root, root.left, root.right).val
print s.lowestCommonAncestor(root, root.left, root.left.right.right).val
