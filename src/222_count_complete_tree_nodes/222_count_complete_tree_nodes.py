# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.countNodesBipartition(root) # O(log^2(n))
        # return self.countNodesBfs(root) # O(n)

    def countNodesBipartition(self, root):
        if (not root):
            return 0
        height,temp = 0,root
        while temp:
            height += 1
            temp = temp.left
        root_subt,count = root,0
        while root_subt:
            height -= 1
            height_subt,temp = 0,root_subt.left
            while temp:
                height_subt += 1
                temp = temp.right
            # the node_number of root_subt and Full Binary subtree of root_subt
            count += 1 << height_subt
            # Check that the left subtree of root_subt is Full Binary Tree, do not switch to verified Full Binary subtree of root_subt
            root_subt = root_subt.right if (height_subt == height) else root_subt.left
        return count

    def countNodesBfs(self, root):
        if (not root):
            return 0
        i,queue = 0,[root]
        while (i < len(queue)):
            node = queue[i]
            if node.right:
                queue.append(node.left)
                queue.append(node.right)
            else:
                if node.left:
                    queue.append(node.left)
                break
            i += 1
        return len(queue)

# debug
s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
print s.countNodes(root)
