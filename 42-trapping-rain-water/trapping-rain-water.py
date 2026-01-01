class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
    
        for i in range(len(height)):
            hei = 0 
            while stack and stack[-1][0] <= height[i]:
                prev_height , _ = stack.pop()
                if stack:
                    res += (min(height[i],stack[-1][0]) - prev_height)*(i - stack[-1][1] - 1)
            stack.append([height[i] , i])
        print(stack)
        return res


