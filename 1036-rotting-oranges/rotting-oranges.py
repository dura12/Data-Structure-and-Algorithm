class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def inbound(row , col):
            return (0<=row<n and 0<=col<m)
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        q = deque()
        fresh = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 2:
                    q.append((row,col))
                if grid[row][col] == 1:
                    fresh += 1
        ans = 0
        while q and fresh > 0:
            for i in range(len(q)):
                row , col = q.popleft()
                for r , c in directions:
                    new_row = r + row
                    new_col = c + col
                    if inbound(new_row,new_col) and grid[new_row][new_col] == 1:
                        fresh -= 1
                        q.append((new_row,new_col))
                        grid[new_row][new_col] = 2
            ans += 1
        return ans   if fresh == 0 else -1

                

        