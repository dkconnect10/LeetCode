class Solution:
    def findNthDigit(self, n):
        length = 1   # digits in number
        count = 9    # numbers in this range
        start = 1    # starting number
        
        # Step 1: find correct range
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        
        # Step 2: find exact number
        num = start + (n - 1) // length
        
        # Step 3: return digit
        return int(str(num)[(n - 1) % length])