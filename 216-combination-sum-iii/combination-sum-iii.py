class Solution:
    def combinationSum3(self, k,n,i=1,path=None,result=None):
        if path is None:
            path= []
        if result is None:
            result = []
        
            
        if len(path)>k or sum(path)>n:
            return 
        
        if len(path)==k:
            if sum(path)==n:
                result.append(path[:])
            return 
        
        if i>9:
            return 
            
        path.append(i)
        self.combinationSum3(k,n,i+1,path,result)
        
        path.pop()
        self.combinationSum3(k,n,i+1,path,result)
        
        return result