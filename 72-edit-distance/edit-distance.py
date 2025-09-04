class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m= len(word2)
        cache = {}
        def dfs(i , j):
            if (i, j) in cache:
                return cache[i,j]
            if i >= n:
                return m - j
            if j >= m:
                return n - i
            operation = 0
            if word1[i] == word2[j]:
                operation += dfs(i + 1 , j + 1)
            else:
                operation += (1 +  min(dfs(i + 1 , j) , dfs(i , j + 1) , dfs(i + 1 , j + 1)))
            cache[i,j] = operation
            return operation
        return dfs(0,0)
        
        

            
