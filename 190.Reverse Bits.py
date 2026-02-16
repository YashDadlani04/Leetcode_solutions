# 16/02/2026 

class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0
        
        result = 0
        for _ in range(32):
            result <<= 1          
            result = result | (n & 1)
            n >>= 1               # n = n >> 1
        
        return result
    