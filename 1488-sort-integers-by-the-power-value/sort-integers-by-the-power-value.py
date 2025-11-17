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
                next_num = val // 2 if val % 2 == 0 else val*3 + 1
                if next_num not in memo:
                    stack.append(next_num)
                else:
                    memo[val] = 1 + memo[next_num]
                    stack.pop()
            return memo[num]
                
        dic = {}
        nums = [[dfs(num) , num] for num in range(lo , hi + 1)]
        nums.sort()
        return nums[k - 1][1]








            