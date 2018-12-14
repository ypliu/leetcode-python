class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        return self.canFinishDfs(numCourses, prerequisites)
        # return self.canFinishBfs(numCourses, prerequisites)

    def canFinishBfs(self, numCourses, prerequisites):
        if (numCourses < 0):
            return False
        elif (numCourses <= 1) or (not prerequisites) or (len(prerequisites) <= 1):
            return True
        indegrees = [0 for _ in range(numCourses)]
        adjacency_list = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            indegrees[edge[0]] += 1
            adjacency_list[edge[1]].append(edge[0])
        srcs = []
        for i in range(numCourses):
            if (0 == indegrees[i]):
                srcs.append(i)
        count = 0
        while (srcs != []):
            src = srcs.pop()
            count += 1
            for d in adjacency_list[src]:
                indegrees[d] -= 1
                if (0 == indegrees[d]):
                    srcs.append(d)
        return (numCourses == count)

    def canFinishDfs(self, numCourses, prerequisites):
        if (numCourses < 0):
            return False
        elif (numCourses <= 1) or (not prerequisites) or (len(prerequisites) <= 1):
            return True
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
        def dfs(h):
            if (0 != is_visited[h]):
                return (is_visited[h] == 1)
            is_visited[h] = -1
            for t in adjacency_list[h]:
                if (not dfs(t)):
                    return False
            is_visited[h] = 1
            return True
        while (srcs != []):
            src = srcs.pop()
            if (not dfs(src)):
                return False
        for i in range(numCourses):
            if (0 == is_visited[i]):
                return False
        return True

# debug
s = Solution()
print s.canFinish(2, [[1,0]])
print s.canFinish(2, [[1,0], [0,1]])
