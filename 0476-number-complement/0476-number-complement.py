class Solution:
    def findComplement(self, num: int) -> int:
        result = ""

        binary = bin(num)[2:]

        for bit in binary:
            if bit=="0":
                result+="1"
            else:
                result+="0"
        return  int(result,2)
                    
        