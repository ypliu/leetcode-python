# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        if n <= 0:
            return []
        return self.helperRecursion(1, n)

    def helperRecursion(self, start, end):
        if start > end:
            return [None]
        elif start == end:
            return [TreeNode(start)]

        forest = []
        for val in range(start, end+1):
            left_subtrees = self.helperRecursion(start, val-1)
            right_subtrees = self.helperRecursion(val+1, end)
            for left_subtree in left_subtrees:
                for right_subtree in right_subtrees:
                    root = TreeNode(val)
                    root.left = left_subtree
                    root.right = right_subtree
                    forest.append(root)
        return forest

# debug
s = Solution()
print len(s.generateTrees(3))
