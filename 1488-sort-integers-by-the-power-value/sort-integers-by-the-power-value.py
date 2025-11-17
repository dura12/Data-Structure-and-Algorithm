class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1 : 0}
        heap = []
        def dfs(num):
            stack = [num]
            while stack:
                val = stack[-1]
                if val in memo:
                    stack.pop()
                    continue
                if val % 2 == 0:
                    next_num = val //2
                else:
                    next_num = val * 3 + 1
                if next_num not in memo:
                    stack.append(next_num)
                else:
                    memo[val] = 1 + memo[next_num]
                    stack.pop()
            return memo[num]
                
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








            