class Solution(object):
    def removeZeros(self, n):
        value = [i for i in str(n) if i != '0']
        n = ''.join(value)
        if n:
            return int(n)
        return 0 
        