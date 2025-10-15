class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        value = x[::-1]
        if x == value:
           return True
        return False
        