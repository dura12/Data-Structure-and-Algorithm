class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u , v in edges:
            graph[v].append(u)
            graph[u].append(v)
        # def dfs(node):
        #     if node == destination:
        #         return True
        #     for nei in graph[node]:
        #         if dfs(nei):
        #             return True
        #     return False
        # return dfs(start)
        visit = set()
        q = deque()
        q.append(source)
        while q:
            node = q.popleft()
            if node == destination:
                return True
            for nei in graph[node]:
                if nei not in visit:
                    q.append(nei)
                    visit.add(nei)
        return False

