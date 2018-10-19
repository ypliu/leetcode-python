# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if not inorder and not postorder:
            return None
        return self.buildTreeRecursion(inorder, postorder)

    def buildTreeRecursion(self, inorder, postorder):
        if 1 == len(inorder):
            return TreeNode(inorder[0])
        val_root = postorder[-1]
        for i in xrange(len(inorder)):
            if inorder[i] == val_root:
                break
        root = TreeNode(val_root)
        if i > 0:
            root.left = self.buildTreeRecursion(inorder[:i], postorder[:i])
        if i < len(inorder)-1:
            root.right = self.buildTreeRecursion(inorder[i+1:], postorder[i:-1])
        return root

# debug
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            queue_temp = []; val_temp = []
            for node in queue:
                val_temp.append(node.val)
                if node.left:
                    queue_temp.append(node.left)
                if node.right:
                    queue_temp.append(node.right)
            queue = queue_temp
            res.append(val_temp)
        return res

s = Solution()
root = s.buildTree([9,3,15,20,7], [9,15,7,20,3])
print s.levelOrder(root)
