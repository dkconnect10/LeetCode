class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        freq=0
        for i in range(n):
            freq^=start+2*i
        return freq 