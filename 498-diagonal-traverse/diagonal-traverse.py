class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        n = len(mat)
        m = len(mat[0])
        sign = 0 
        for i in range(n):
            temp = []
            row = i
            col = 0
            while row >= 0 and col < m:
                temp.append(mat[row][col])
                row -= 1 
                col += 1
            if sign == 0:
                ans.extend(temp)
                sign = 1
            else:
                ans.extend(temp[::-1])
                sign = 0
        for i in range(1 , m):
            row = n - 1
            col = i
            temp = []
            while row >= 0 and col < m:
                temp.append(mat[row][col])
                row -=1 
                col += 1

            if sign == 0:
                ans.extend(temp)
                sign = 1
            else:
                ans.extend(temp[::-1])
                sign = 0
        return ans


            
                
                