class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for u , v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        order = []
        visit = set()
        while q:
            node = q.popleft()
            order.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                    visit.add(nei)
        return order if len(order) == numCourses else []

        

        