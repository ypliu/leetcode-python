# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        res = []; is_reverse = False
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
            if is_reverse:
                val_temp.reverse()
            res.append(val_temp)
            is_reverse = not is_reverse
        return res

# debug
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s = Solution()
print s.zigzagLevelOrder(root)
