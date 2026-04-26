class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for letter in s:
            if letter == "*":
                if not stack:
                    continue
                stack.pop()
                continue
            stack.append(letter)
        return "".join(stack)