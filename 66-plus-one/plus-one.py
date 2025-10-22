class Solution(object):
    def plusOne(self, digits):
       value = "".join(map(str,digits))
       mvalue = str(int(value)+1)
       value = [int(i) for i in mvalue]
       return value