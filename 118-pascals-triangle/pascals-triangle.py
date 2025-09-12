class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        self.ans = []
        def dfs(row):
            if row == 0:
                return []
            if row == 1:
                return [[1]]
            res = dfs(row - 1)
            res.append([1] + [res[-1][i] + res[-1][i+1] for i in range(len(res[-1])-1)] + [1])
            return res
        return dfs(numRows)


