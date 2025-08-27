class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(i , j):
            if (i,j) in memo:
                return memo[i,j]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if i >= len(s):
                for k in range(j , len(p)):
                    if p[k] != "*":
                        memo[i,j] = False
                        return memo[i,j]
                memo[i,j] = True
                return memo[i,j]
            match =(p[j] == s[i] or p[j] == "?")
            if p[j] == "*":
                memo[i,j] =  dfs(i + 1 , j) or dfs(i , j + 1)
                return memo[i,j]
            if match:
                memo[i,j] =  dfs(i+1 , j + 1)
                return memo[i,j]
            memo[i,j] = False
            return memo[i,j]
        return dfs(0,0)
            
