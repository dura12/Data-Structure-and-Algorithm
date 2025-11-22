class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = 0
        k = x
        while k > 0:
            lst = k% 10
            num = num * 10 + lst
            k //= 10
        return num == x

