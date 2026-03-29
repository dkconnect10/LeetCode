class Solution:
    def kthCharacter(self, k,string = "a"):
        if len(string)>=k:
            return string[k-1]
        for i in string:
            string+=chr(ord(i)+1)
        return self.kthCharacter(k,string)