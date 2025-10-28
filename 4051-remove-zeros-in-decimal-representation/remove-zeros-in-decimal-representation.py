class Solution(object):
    def removeZeros(self, n):
        s = str(n).replace('0','')   
        return int(s) if s else 0