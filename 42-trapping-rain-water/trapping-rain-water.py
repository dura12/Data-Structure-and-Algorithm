class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        height = height[::-1]
        for i , num in enumerate(height):
            while stack and height[stack[-1]] <= num:
                index = stack.pop()
                if stack:
                    g = min(num , height[stack[-1]]) - height[index]
                    ans +=  g*(i - stack[-1] - 1)
            stack.append(i)
        return ans




