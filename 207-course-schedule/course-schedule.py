class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)
        color = [0]*numCourses
        def dfs(node):
            if color[node] == 1:
                return False
            color[node] = 1
            for nei in graph[node]:
                if color[nei] != 2:
                    if not dfs(nei):
                        return False
            color[node] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
                