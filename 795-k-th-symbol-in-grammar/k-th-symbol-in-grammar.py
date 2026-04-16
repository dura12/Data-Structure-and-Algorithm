class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def rec(nn, k):
            if nn == 1:
                return 0
            
            mid = 2 ** (nn - 2)
            
            if k <= mid:
                return rec(nn - 1, k)
            else:
                return 1 - rec(nn - 1, k - mid)
        
        return rec(n, k)