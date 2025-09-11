class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dfs(i,j):
            if i + j == len(s3):
                return j == len(s2) and i == len(s1)
            if i >= len(s1):
                return  s3[i+j:] == s2[j:]
            if j >= len(s2):
                return  s3[i+j:] == s1[i:]
               
            if s1[i] == s3[i+j]:
                if dfs(i + 1 , j):
                    return True
            if s2[j] == s3[i+j]:
                if dfs(i , j + 1):
                    return True
            return False
        return dfs(0,0)
            


