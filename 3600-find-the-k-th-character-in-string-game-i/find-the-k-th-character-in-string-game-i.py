class Solution:
    def kthCharacter(self, k):
        string = "a"
        
        while len(string)<k:
            for i in string:
                string+=chr(ord(i)+1)
        return string[k-1]