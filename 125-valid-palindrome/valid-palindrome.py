class Solution(object):
    def isPalindrome(self, s):
        strings = []
        for i in s:
            if ('a' <= i <= 'z') or ('A' <= i <= 'Z') or ('0' <= i <= '9'):
                strings.append(i)
        char_value = (''.join(strings)).lower()
        
        left = 0
        right = len(char_value)-1
        
        while left < right:
            if char_value[left] != char_value[right]:
                print(char_value[left],char_value[right])
                return False
            left += 1
            right -= 1
        return True

