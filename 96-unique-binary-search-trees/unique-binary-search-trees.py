class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def dfs(left , right):
            if left >= right:
                return 1
            ans = 0
            print(left , right)
            for i in range(left , right + 1):
                l = dfs(left , i - 1)
                r = dfs(i + 1 , right)
                ans += (l*r)
            return ans
        return dfs(1, n)
