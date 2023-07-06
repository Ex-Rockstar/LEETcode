class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        a=0;
        b=int(sqrt(c))
        if(c<0):
            return False
        while(a<=b):
            if(a*a + b*b == c):
                return True
            elif(a*a + b*b < c):
                a+=1
            else:
                b-=1
        return False
            
        
        
        