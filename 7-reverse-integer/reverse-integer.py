class Solution(object):
    def reverse(self, x):
        is_negative = x < 0
        num = str(abs(x))
        value = num[::-1]
        reversed_num = int(value)
        if is_negative:
            reversed_num = -reversed_num
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0    
        return reversed_num
obj = Solution()  
obj.reverse(1534236469)