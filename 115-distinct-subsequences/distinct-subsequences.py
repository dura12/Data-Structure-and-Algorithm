class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dfs(i, j):
            if j == len(t): 
                return 1
            if i == len(s): 
                return 0
            ans = dfs(i + 1, j) 
            if s[i] == t[j]:
                ans += dfs(i + 1, j + 1)
            return ans
        
        return dfs(0, 0)
