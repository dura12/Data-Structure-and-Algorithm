class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        heap = []
        def dfs(num):
            if num in memo:
                return memo[num]
            if num == 1:
                return 0
            count = 0
            if num % 2 == 0:
                count =  1 + dfs(num // 2)
            if num % 2 != 0:
                count = 1 + dfs(3*num + 1)
            memo[num] = count
            return count
        dic = {}
        for i in range(lo , hi + 1):
            count = 0
            if i in memo:
                count = memo[i]
            else:
                count = dfs(i)
            if len(heap) == k:
                if heap[0] < (-count , -i):
                    heappop(heap)
                    heappush(heap , (-count , -i))
            else:
                heappush(heap , (-count , -i))
        return -heap[0][1]








            