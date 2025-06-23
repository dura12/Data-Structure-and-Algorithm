class Solution:
    digit: list[int] = [0] * 100
    def is_palindrom(self, n: int, k: int) -> bool:
        length: int = -1
        while n:
            length += 1
            self.digit[length] = n % k
            n //= k
        left: int = 0
        right: int = length
        while left < right:
            if self.digit[left] != self.digit[right]: return False
            left += 1
            right -= 1
        return True
    
    def kMirror(self, k: int, n: int) -> int:
        self.digit = [0] * 100
        left: int = 1
        valid: int = 0
        output: int = 0
        while valid < n:
            right: int = left * 10
            for op in range(2):
                i: int = left
                while i < right and valid < n:
                    combined: int = i
                    x: int = [i // 10, i][op != 0]
                    i += 1
                    while x:
                        combined = combined * 10 + x % 10
                        x //= 10
                    if self.is_palindrom(combined, k):
                        valid += 1
                        output += combined
            left = right
        return output