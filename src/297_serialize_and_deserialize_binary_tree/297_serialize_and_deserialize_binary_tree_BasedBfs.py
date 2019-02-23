# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        q = [root]; str_res = ""
        while q:
            q_temp = []
            for node in q:
                if node:
                    str_res += ',' + str(node.val)
                    q_temp.append(node.left)
                    q_temp.append(node.right)
                else:
                    str_res += ",None"
            q = q_temp
        return str_res[1:]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if (not data) or (data == "None"):
            return None
        values = data.split(',')
        q_nodes = [TreeNode(int(values[0]))]
        indx_parent = 0; indx_child = 1
        while (indx_parent < len(q_nodes)):
            if (values[indx_child] != "None"):
                node = TreeNode(int(values[indx_child]))
                q_nodes[indx_parent].left = node
                q_nodes.append(node)
            indx_child += 1
            if (values[indx_child] != "None"):
                node = TreeNode(int(values[indx_child]))
                q_nodes[indx_parent].right = node
                q_nodes.append(node)
            indx_child += 1
            indx_parent += 1
        return q_nodes[0]

# debug
# Your Codec object will be instantiated and called as such:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
codec = Codec()
codec.deserialize(codec.serialize(root))
