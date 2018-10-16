# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        if not root:
            return
        first_node, second_node = self.inorderTraversalStack(root)
        if first_node and second_node:
            first_node.val, second_node.val = second_node.val, first_node.val
        #print first_node.val, second_node.val

    def inorderTraversalStack(self, root):
        pre_node = first_node = second_node = None
        temp = root; stack = []
        while temp or stack:
            while temp:
                stack.append(temp)
                temp = temp.left
            temp = stack.pop()
            if pre_node and pre_node.val >= temp.val:
                if not first_node:
                    first_node = pre_node
                second_node = temp
            pre_node = temp
            temp = temp.right
        return first_node, second_node

# debug
s = Solution()
root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(2)
s.recoverTree(root)
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)
s.recoverTree(root)
