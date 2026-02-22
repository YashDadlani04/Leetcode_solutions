#22/02/2026


class Solution:
    def binaryGap(self, n: int) -> int:
        cb=0
        pb=-1
        result=0

        while n>0:
            if n&1:
                if pb != -1:
                    result = max(result, cb - pb)
                pb = cb

            cb += 1
            n >>= 1      

        return result        