class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return 
        
        n, m = len(board), len(board[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        inbound = lambda x, y: 0 <= x < n and 0 <= y < m
        
        def dfs(row, col):
            board[row][col] = "K"
            for r, c in directions:
                nrow, ncol = r + row, c + col
                if inbound(nrow, ncol) and board[nrow][ncol] == "O":
                    dfs(nrow, ncol)
            return 
        
        # 1. Mark safe regions starting from borders
        for i in range(n):
            for j in range(m):
                # Optimization: Only start DFS if we are on a border
                if (i == 0 or j == 0 or i == n - 1 or j == m - 1):
                    if board[i][j] == "O":
                        dfs(i, j)
        
        # 2. Final Sweep
        for i in range(n):
            for j in range(m):
                if board[i][j] == "K":
                    board[i][j] = "O" # Restore safe cells
                elif board[i][j] == "O":
                    board[i][j] = "X" # Capture surrounded cells