class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        temp = []
        for i in range(n):
            temp.append(start+2*i)
        
        freq=0
        for val in temp:
            freq^=val
        return freq 