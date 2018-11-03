# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):

        if not node:
            return None
        nodes_dict = {}
        return self.cloneGraphDfs(node, nodes_dict)

    def cloneGraphDfs(self, node, nodes_dict):
        if not node:
            return None
        elif not (node in nodes_dict):
            nodes_dict[node] = UndirectedGraphNode(node.label)
        for neighbor in node.neighbors:
            if not (neighbor in nodes_dict):
                nodes_dict[node].neighbors.append(self.cloneGraphDfs(neighbor, nodes_dict))
            else:
                nodes_dict[node].neighbors.append(nodes_dict[neighbor])
        return nodes_dict[node]

# debug
node = UndirectedGraphNode(1)
s = Solution()
s.cloneGraph(node)
