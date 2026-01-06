class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        nag=[]

        for num in nums:
            if num<0:
                nag.append(num)
            else:    
                pos.append(num)
               
        if len(pos)>len(nag):
            for i in range(len(nag)):
                nums[i*2]=pos[i]
                nums[i*2+1]=nag[i]
                
            index=len(nag)*2
            
            for j in range(i+1,len(pos)):
                nums[index]=pos[j]
                index+=1
        else:
            for i in range(len(pos)):
                nums[i*2]=pos[i]
                nums[i*2+1]=nag[i]

            index = len(pos)*2
            
            for j in range(i+1,len(nag)):
                nums[index]=nag[j]
                index+=1
        return nums