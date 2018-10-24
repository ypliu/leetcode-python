# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        # based on BFS
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            queue_temp = []
            for node,val_sum,path in queue:
                if not node.left:
                    if node.right:
                        queue_temp.append((node.right, node.right.val + val_sum, path + [node.right.val]))
                    elif (val_sum == sum):
                        res.append(path)
                else:
                    queue_temp.append((node.left, node.left.val + val_sum, path + [node.left.val]))
                    if node.right:
                        queue_temp.append((node.right, node.right.val + val_sum, path + [node.right.val]))
            queue = queue_temp
        return res

# debug
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
s = Solution()
print s.pathSum(root, 22)
