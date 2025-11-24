class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        start = 0
        end = len(graph) - 1
        ans = []
        seen =set()
        def dfs(node , path):
            if node == end:
                ans.append(path.copy())
                return 
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    path.append(nei)
                    dfs(nei , path)
                    path.pop()
            seen.remove(node)
            return 
        dfs(0 , [0])
        return ans
            
                    