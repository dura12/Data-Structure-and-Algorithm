class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u , v in edges:
            graph[v].append(u)
            graph[u].append(v)
        def dfs(node , visit):
            #base
            if node == destination:
                return True
            visit.add(node)
            for nei in graph[node]:
                if nei not in visit:
                    if dfs(nei,visit):
                        return True
            return False
        return dfs(source,set())
                       



        # stack = [source]
        # visit = set([source])
        # while stack:
        #     node = stack.pop()
        #     if node == destination:
        #         return True
        #     for nei in graph[node]:
        #         if nei not in visit:
        #             stack.append(nei)
        #             visit.add(nei)
        # return False
                