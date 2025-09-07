class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def searchMaxArea(heights):
            stack = []
            ans = 0
            for i in range(len(heights)):
                lat = i
                while stack and stack[-1][0] > heights[i]:
                    h, index= stack.pop()
                    ans = max(ans , h*(i - index))
                    lat = index
                stack.append([heights[i] ,lat] )
            n = len(heights)
            for i , j in stack:
                ans = max(ans , i*(n - j ))
            return ans
        result = 0
        n = len(matrix)
        m = len(matrix[0])
        heights = [0]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
            result = max(result ,searchMaxArea(heights) )
        return result


                