# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not preorder and not inorder:
            return None
        elif len(preorder) != len(inorder):
            print "Error-1! The lengths of 'preorder' and 'inorder' are different!"
            return None
        return self.buildTreeRecursion(preorder, inorder)

    def buildTreeRecursion(self, preorder, inorder):
        if len(preorder) != len(inorder):
            print "Error-2! The lengths of 'preorder' and 'inorder' are different!"
            return None
        if 1 == len(preorder) and 1 == len(inorder):
            if preorder[0] == inorder[0]:
                return TreeNode(preorder[0])
            else:
                print "Error-3! The values of leaf corresponding to 'preorder' and 'inorder' are different!"
                return None
        val_root = preorder[0]
        for i in xrange(len(inorder)):
            if inorder[i] == val_root:
                break
        else:
            print "Error-4! The values of leaf corresponding to 'preorder' and 'inorder' are different!"
            return None
        root = TreeNode(val_root)
        if i > 0:
            root.left = self.buildTreeRecursion(preorder[1:i+1], inorder[:i])
        if i < len(inorder)-1:
            root.right = self.buildTreeRecursion(preorder[i+1:], inorder[i+1:])
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
#root = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
root = s.buildTree([1,2], [1,2])
print s.levelOrder(root)
