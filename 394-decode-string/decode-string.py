class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                digit = ""
                stack.pop()
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                stack.append(int(digit)*substring)
        return "".join(stack)