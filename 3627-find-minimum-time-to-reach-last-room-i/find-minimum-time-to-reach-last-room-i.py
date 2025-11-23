class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        processed = set()
        q =[[0,0,0]]
        n = len(moveTime)
        m = len(moveTime[0])
        min_time = [[float('inf')] * m for _ in range(n)]
        min_time[0][0] = 0
        def inbound(row , col):
            return 0 <= row < n and 0 <= col < m
        while q:
            r , c , t = heappop(q)
            if r == n - 1 and c == m - 1:
                return t
            if min_time[r][c] < t:
                continue 
            for i , j in [(0,1) ,(1,0) , (-1 , 0) , (0 , -1)]:
                nrow = i + r
                ncol = j + c
                if inbound(nrow , ncol):
                    time = max(t , moveTime[nrow][ncol]) + 1
                    if  time < min_time[nrow][ncol]:
                        heappush(q , [nrow , ncol , time])
                        min_time[nrow][ncol] = time
        

        return -1