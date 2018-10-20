# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums:
            return None
        return self.sortedSubArrayToBSTRecursion(nums, 0, len(nums)-1)

    def sortedSubArrayToBSTRecursion(self, nums, start, end):
        if start == end:
            return TreeNode(nums[start])
        mid = (start + end + 1) >> 1
        root = TreeNode(nums[mid])
        root.left = self.sortedSubArrayToBSTRecursion(nums, start, mid-1)
        if mid < end:
            root.right = self.sortedSubArrayToBSTRecursion(nums, mid+1, end)
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
root = s.sortedArrayToBST([-10,-3,0,5,9])
print s.levelOrder(root)
