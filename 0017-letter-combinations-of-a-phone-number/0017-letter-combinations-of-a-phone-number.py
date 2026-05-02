class Solution:
    def helper(self,digits,nums,i=0,path=None,result=None):
        if path is None:
            path = []
        if result is None:
            result =[]
            
        if i==len(digits):
            result.append(''.join(path))
            return 
        for num in nums[digits[i]]:
            path.append(num)
            self.helper(digits,nums,i+1,path,result)
            path.pop()
        return result
    def letterCombinations(self,digits):
        if len(digits)<1:
            return digits
        
        nums = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        
        return self.helper(digits,nums)