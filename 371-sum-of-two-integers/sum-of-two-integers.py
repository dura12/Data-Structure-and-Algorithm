class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask to handle Python's infinite integer behavior
        mask = 0xffffffff
        
        # Base Case: No carry left
        if b == 0:
            # If a is negative in 32-bit sense, return it correctly
            return a if a <= 0x7fffffff else ~(a ^ mask)
        
        # Logic:
        # 1. (a ^ b) adds digits without carrying
        # 2. (a & b) << 1 calculates the carry
        # 3. & mask ensures we stay within 32 bits
        
        sum_without_carry = (a ^ b) & mask
        carry = ((a & b) << 1) & mask
        
        return self.getSum(sum_without_carry, carry)