class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len((s))
        res = []
        def is_paind(sub_string):
            i = 0
            j = len(sub_string) - 1
            while i < j:
                if sub_string[i] != sub_string[j]:
                    return False
                i += 1
                j -= 1
            return True
        def dfs(i , curr):
            if i == n:
                res.append(curr[:])
                return 
            for j in range( i , n):
                if is_paind(s[i: j + 1]):
                    curr.append(s[i:j + 1])
                    dfs(j + 1 ,curr )
                    curr.pop()
            return 
        dfs(0 , [])
        return res
                