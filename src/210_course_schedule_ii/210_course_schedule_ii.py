class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        return self.findOrderDfs(numCourses, prerequisites)

    def findOrderDfs(self, numCourses, prerequisites):
        if (numCourses < 0):
            return []
        elif (numCourses <= 1) or (not prerequisites) or (len(prerequisites) == 0):
            return [i for i in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        adjacency_list = [[] for _ in range(numCourses)]
        is_visited = [0 for _ in range(numCourses)]
        for edge in prerequisites:
            indegrees[edge[0]] += 1
            adjacency_list[edge[1]].append(edge[0])
        srcs = []
        for i in range(numCourses):
            if (0 == indegrees[i]):
                srcs.append(i)
        sol = []
        def dfs(h, path):
            if (0 != is_visited[h]):
                return (is_visited[h] == 1)
            is_visited[h] = -1
            for t in adjacency_list[h]:
                if (not dfs(t, path)):
                    return False
            is_visited[h] = 1
            path.append(h)
            return True
        while (srcs != []):
            src = srcs.pop()
            p = []
            if (not dfs(src, p)):
                return []
            sol += p
        for i in range(numCourses):
            if (0 == is_visited[i]):
                return []
        return sol[::-1]

# debug
s = Solution()
print s.findOrder(2, [[1,0]])
print s.findOrder(2, [[1,0], [0,1]])
print s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
