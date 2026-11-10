
class Solution:
    def validPalindrome(self, s):
        orignal_str = list(s)
        target = False
        
        i, j = 0, len(orignal_str)-1
        
        while i <= j:
            if orignal_str[i] != orignal_str[j]:
                target = True
                break
            i += 1
            j -= 1
        
        if target:
            for k in [i, j]:
                copy_str = orignal_str[:]
                copy_str.pop(k)
                
                i, j = 0, len(copy_str)-1
                is_palindrome = True
                
                while i <= j:
                    if copy_str[i] != copy_str[j]:
                        is_palindrome = False
                        break
                    i += 1
                    j -= 1
                
                if is_palindrome:
                    return True
                    
            return False
        
        else:
            return True
